#!/home/m0rtzz/Program_Files/anaconda3/envs/VisionVoyage/bin/python3

import carla
from carla import ColorConverter as cc
import random
import queue
import numpy as np
import os
import logging
import dataset_utils
import fisheye_utils
import cv2
import fnmatch
import generate_traffic

'''
Data collector for collecting point clouds of
different setups of sensors.

'''

CLIENT_HOST = '127.0.0.1'
CLIENT_PORT = 2000
TRAFFIC_MANAGER_PORT = 8000


# # TAG
# def process_semantic(image):
#     image.convert(carla.ColorConverter.CityScapesPalette)
#     # array = np.frombuffer(image.raw_data, dtype=np.dtype("uint8"))
#     # array = np.reshape(array, (image.height, image.width, 4))
#     # array = array[:, :, :3]
#     return image

class DataCollector:
    def __init__(self, collector_config, logging_path='log'):
        set = None
        self.initialize_nums = 0
        self.bus_nums = 0
        self.two_wheels_nums = 0
        self.bicycle_nums = 0
        self.motorcycle_nums = 0
        self.logger = dataset_utils.create_logger()
        self.collector_config = collector_config
        self.map = collector_config.get('MAP', 'Town10HD_Opt')
        self.hero_vehicle_name = collector_config.get('HERO_VEHICLE', 'vehicle.tesla.model3')
        self.num_of_env_vehicles = collector_config.get('NUM_OF_ENV_VEHICLES', 0)
        self.num_of_env_pedestrians = collector_config.get('NUM_OF_ENV_PEDESTRIANS', 0)
        self.data_save_path = collector_config.get('DATA_SAVE_PATH', './images/my_images/fisheye_dataset')
        self.env_vehicles_points = []
        if not os.path.exists(self.data_save_path):
            os.mkdir(self.data_save_path)

        self.sensor_group_list = collector_config['SENSOR_GROUP_LIST']

        self.reference_sensor_transform = None

        self.total_timestamp = collector_config.get('TOTAL_TIMESTAMPS', 2000)
        self.save_interval = collector_config.get('SAVE_INTERVAL', None)
        self.start_timestamp = collector_config.get('START_TIMESTAMP', 0)

        self.save_lane = collector_config.get('SAVE_LANE', False)

        self.client = None
        self.world = None
        self.traffic_manager = None
        # self.sensor_actors = []
        # self.sensor_actors_ = []
        self.sensor_actors_1 = []
        self.sensor_actors_1_ = []
        self.sensor_actors_2 = []
        self.sensor_actors_2_ = []
        self.sensor_actors_3 = []
        self.sensor_actors_3_ = []
        self.sensor_actors_4 = []
        self.sensor_actors_4_ = []
        # self.sensor_queues = []
        # self.sensor_queues_ = []
        self.sensor_queues_1 = []
        self.sensor_queues_1_ = []
        self.sensor_queues_2 = []
        self.sensor_queues_2_ = []
        self.sensor_queues_3 = []
        self.sensor_queues_3_ = []
        self.sensor_queues_4 = []
        self.sensor_queues_4_ = []
        self.hero_vehicle = None
        self.env_vehicles = []
        self.env_pedestrians = []
        self.frame = None

    def set_synchronization_world(self, synchronous_mode=True, delta_seconds=0.05):
        # Enables synchronous mode for world
        settings = self.world.get_settings()
        settings.synchronous_mode = synchronous_mode
        settings.fixed_delta_seconds = delta_seconds
        self.world.apply_settings(settings)

    def set_synchronization_traffic_manager(self, traffic_manager, global_distance=3, hybrid_physics_mode=True, synchronous_mode=True):
        # Set up the TM in synchronous mode
        traffic_manager.set_synchronous_mode(synchronous_mode)
        traffic_manager.set_global_distance_to_leading_vehicle(global_distance)
        traffic_manager.set_hybrid_physics_mode(hybrid_physics_mode)
        traffic_manager.set_respawn_dormant_vehicles(True)

    def set_hero_vehicle(self, set_autopilot=True):
        hero_bp = self.world.get_blueprint_library().find(self.hero_vehicle_name)
        # hero_bp.set_attribute('color', '0, 0, 0')  # set hero vehicle color to black
        hero_bp.set_attribute('color', '255, 255, 255')  # set hero vehicle color to black
        hero_bp.set_attribute('role_name', 'autopilot')

        transform = random.choice(self.world.get_map().get_spawn_points())
        self.hero_vehicle = self.world.spawn_actor(hero_bp, transform)
        # set_desired_speed(self,)
        if set_autopilot:
            self.hero_vehicle.set_autopilot(True, TRAFFIC_MANAGER_PORT)

        vehicle = self.world.get_actor(self.hero_vehicle.id)
        # self.client = carla.Client('localhost', 2000)
        self.traffic_manager = self.client.get_trafficmanager()
        self.traffic_manager.set_desired_speed(vehicle, 100.0)
        self.logger.info('Set hero vehicle Done!')

    # def set_env_pedestrians(self):
    #     # 生成行人
    #     spawn_points = self.world.get_map().get_spawn_points()
    #     pedestrians = []
    #     for i in range(50):
    #         spawn_point = spawn_points[i % len(spawn_points)]

    #         # npc = self.world.spawn_actor(carla.Transform(spawn_point.location), "walker.pedestrian.0001")
    #         transform = carla.Transform(spawn_point.location, spawn_point.rotation)
    #         npc = self.world.spawn_actor(carla.ActorBlueprint("walker.pedestrian.0001"), transform)

    #         npc.set_walk_speed(0.5)
    #         npc.set_destination((spawn_point.location + carla.Location(x=1, y=1, z=0)))
    #         pedestrians.append(npc)

    #     # 控制行人的移动
    #     for i, pedestrian in enumerate(pedestrians):
    #         if i % 2 == 0:
    #             pedestrian.set_walk_speed(0.75)
    #             pedestrian.set_destination(
    #                 (spawn_points[(i + 1) % len(spawn_points)].location + carla.Location(x=1, y=1, z=0)))
    #         else:
    #             pedestrian.set_walk_speed(0.25)
    #             pedestrian.set_destination(
    #                 (spawn_points[(i - 1) % len(spawn_points)].location + carla.Location(x=1, y=1, z=0)))

    #     # 监控行人的状态
    #     while True:
    #         for pedestrian in pedestrians:
    #             location = pedestrian.get_location()
    #             if location.x > 5:
    #                 pedestrian.set_destination((spawn_points[0].location + carla.Location(x=1, y=1, z=0)))

    # def set_env_pedestrians(self, num_walkers):
    #     walker_controller_bp = self.world.get_blueprint_library().find('controller.ai.walker')
    #     # num_walkers = self.num_of_env_pedestrians
    #     for _ in range(num_walkers):
    #         spawn_point = carla.Transform()
    #         walker_controller = self.world.spawn_actor(walker_controller_bp, spawn_point)

    #         # Initialize the AI controller
    #         walker_controller.start()

    #         # Set a random target location for the walker
    #         target_location = self.world.get_random_location_from_navigation()
    #         walker_controller.go_to_location(target_location)

    #         # Set a random maximum speed for the walker
    #         max_speed = 1 + random.random()  # Between 1 and 2 m/s
    #         walker_controller.set_max_speed(max_speed)

    # def set_env_pedestrians(self):
    #     walker_controller_bp = self.world.get_blueprint_library().find('controller.ai.walker')
    #     vehicle_locations = [v.get_location() for v in self.env_vehicles]
    #     pedestrian_spawn_points = [p for p in self.world.get_map().get_spawn_points()
    #                                if p not in self.env_vehicles_points]
    #     for _ in range(self.num_of_env_pedestrians):
    #         spawn_point = None
    #         while not spawn_point:
    #             # Generate a random location for the walker
    #             target_location = self.world.get_random_location_from_navigation()
    #             # Check if this location overlaps with any vehicle locations
    #             overlap = False
    #             for loc in vehicle_locations:
    #                 if target_location.distance(loc) < 5:  # Adjust the distance threshold as needed
    #                     overlap = True
    #                     break
    #             # Check if this location overlaps with any pedestrian spawn points
    #             if target_location in pedestrian_spawn_points:
    #                 overlap = True
    #             if not overlap:
    #                 spawn_point = carla.Transform(target_location)
    #         walker_controller = self.world.spawn_actor(walker_controller_bp, spawn_point)
    #         # Initialize the AI controller
    #         walker_controller.start()
    #         # Set a random target location for the walker
    #         walker_target_location = self.world.get_random_location_from_navigation()
    #         walker_controller.go_to_location(walker_target_location)
    #         # Set a random maximum speed for the walker
    #         max_speed = 1 + random.random()  # Between 1 and 2 m/s
    #         walker_controller.set_max_speed(max_speed)

    def set_env_pedestrians(self):
        walker_controller_bp = self.world.get_blueprint_library().filter('controller.ai.walker')
        for _ in range(self.num_of_env_pedestrians):
            # Generate random spawn point for the walker
            spawn_point = carla.Transform()
            loc = self.world.get_random_location_from_navigation()
            if loc is not None and loc not in self.env_vehicles_points:
                spawn_point.location = loc
                # print(loc)
                # Spawn the walker object
                walker_bp = random.choice(walker_controller_bp)
                if walker_bp.has_attribute('is_invincible'):
                    walker_bp.set_attribute('is_invincible', 'false')
                if walker_bp.has_attribute('speed'):
                    max_speed = 1 + random.random()  # Between 1 and 2 m/s
                    walker_bp.set_attribute('speed', max_speed)

                walker = self.world.spawn_actor(walker_bp, spawn_point)

                # Spawn the walker controller object
                walker_controller = self.world.spawn_actor(walker_bp, carla.Transform())

                walker_controller.attach_to_actor(walker)

                # Initialize the AI controller
                walker_controller.start()

                # Set a random target location for the walker
                target_location = self.world.get_random_location_from_navigation()
                walker_controller.go_to_location(target_location)

                # Set a random maximum speed for the walker
                walker_controller.set_max_speed(max_speed)

                # Add the walker and controller to the environment actors list
                self.env_actors.append(walker)
                self.env_actors.append(walker_controller)

    def set_traffic_lights_to_green(self):
        # 连接到Carla服务器
        client = carla.Client('localhost', 2000)
        client.set_timeout(10.0)

        # 获取世界对象和所有演员
        # world = client.get_world()
        world = self.world
        actors = world.get_actors()

        # 过滤出所有的交通灯演员
        light_actors = actors.filter('*traffic_light*')

        # 将所有交通灯设置为绿色并冻结
        for light_actor in light_actors:
            # light_actor.set_state(carla.TrafficLightState.Green)
            light_actor.set_green_time(10.0)
            light_actor.set_red_time(1.0)
            # light_actor.freeze(True)

    def set_env_vehicles(self):
        vehicle_blueprints = self.world.get_blueprint_library().filter('*vehicle*')
        filtered_list = [bp for bp in vehicle_blueprints if not fnmatch.fnmatch(bp.id, 'vehicle.tesla.*')]
        bus_bp = self.world.get_blueprint_library().find('vehicle.mitsubishi.fusorosa')
        SpawnActor = carla.command.SpawnActor
        SetAutopilot = carla.command.SetAutopilot
        FutureActor = carla.command.FutureActor

        # filtered_blueprints_bicycle = [bp for bp in filtered_list if any(fnmatch.fnmatch(bp.id, pattern) for pattern in [
        #     "vehicle.diamondback.century", "vehicle.gazelle.omafiets"])]

        # filtered_blueprints_motorcycle = [bp for bp in filtered_list if any(fnmatch.fnmatch(bp.id, pattern) for pattern in [
        #     "vehicle.harley-davidson.low_rider", "vehicle.yamaha.yzf"])]

        filtered_blueprints_bicycle = [bp for bp in filtered_list if
                                       bp.id in ['vehicle.diamondback.century', 'vehicle.gazelle.omafiets']]

        filtered_blueprints_motorcycle = [bp for bp in filtered_list if
                                          bp.id in ['vehicle.harley-davidson.low_rider', 'vehicle.yamaha.yzf']]

        batch = []

        spawn_points = self.world.get_map().get_spawn_points()
        # random.shuffle(spawn_points)  # 随机打乱生成点顺序
        self.env_vehicles_points = spawn_points
        # print(spawn_points)
        self.logger.info(f'Total blueprints: {len(vehicle_blueprints)}')
        self.logger.info(f'Total spawn points: {len(spawn_points)}')
        for i, transform in enumerate(spawn_points):
            # if (i >= self.num_of_env_vehicles) and (self.bus_nums == 7 and self.bicycle_nums == 20 and self.motorcycle_nums == 20):
            if (i >= self.num_of_env_vehicles):
                break

            bicycle_bp = random.choice(filtered_blueprints_bicycle)
            motorcycle_bp = random.choice(filtered_blueprints_motorcycle)
            # print("bicycle_bp", bicycle_bp)
            # print("motorcycle_bp", motorcycle_bp)
            # print(vehicle_bp)

            # # 太卡了笔记本
            # if self.bus_nums < 7:
            #     vehicle_bp = bus_bp
            #     self.bus_nums += 1
            # elif self.bicycle_nums < 20:
            #     vehicle_bp = bicycle_bp
            #     self.bicycle_nums += 1
            # elif self.motorcycle_nums < 20:
            #     vehicle_bp = motorcycle_bp
            #     self.motorcycle_nums += 1
            # elif (self.bus_nums == 7 and self.bicycle_nums == 20 and self.motorcycle_nums == 20):
            # vehicle_bp = random.choice(filtered_list)

            vehicle_bp = random.choice(filtered_list)
            # has no idea about the meaning of driver_id
            if vehicle_bp.has_attribute('driver_id'):
                driver_id = random.choice(vehicle_bp.get_attribute('driver_id').recommended_values)
                vehicle_bp.set_attribute('driver_id', driver_id)

            vehicle_bp.set_attribute('role_name', 'autopilot')
            # spawn the cars and set their autopilot all together
            batch.append(SpawnActor(vehicle_bp, transform).then(SetAutopilot(FutureActor, True, TRAFFIC_MANAGER_PORT)))

        for response in self.client.apply_batch_sync(batch, True):
            if response.error:
                self.logger.info(response.error)
            else:
                self.env_vehicles.append(self.world.get_actor(response.actor_id))

                # print(response.actor_id)

        # print("bus_nums", self.bus_nums)
        # print("bicycle_nums", self.bicycle_nums)
        # print("motorcycle_nums", self.motorcycle_nums)
        # print("env_vehicles", self.env_vehicles)

        # NOTE: 汽车加速
        for actor_id in self.env_vehicles:
            # print(actor_id)
            vehicle = self.world.get_actor(actor_id.id)
            # self.client = carla.Client('localhost', 2000)
            self.traffic_manager = self.client.get_trafficmanager()
            self.traffic_manager.set_desired_speed(vehicle, 100.0)
        self.logger.info('Set env vehicles Done!')

    def set_sensors(self):
        SpawnActor = carla.command.SpawnActor
        batch = []
        batch_ = []
        for sensor_group in self.sensor_group_list:
            # path = os.path.join(self.data_save_path, sensor_group["NAME"])
            # if not os.path.exists(path):
            #     os.mkdir(path)
            ################# Special Setup for Fisheye #################

            def set_sensors_fisheye(sensor_group, batch):
                Attachment = carla.AttachmentType
                sensor_transform = sensor_group['TRANSFORM']
                location = carla.Location(x=sensor_transform.get(
                    'x', 0), y=sensor_transform.get('y', 0), z=sensor_transform.get('z', 0))

                roll = sensor_transform.get('roll', 0)
                pitch = sensor_transform.get('pitch', 0)
                yaw = sensor_transform.get('yaw', 0)

                # # NOTE: 向前
                # location = carla.Location(x=self.hero_vehicle.bounding_box.extent.x,
                #                           y=sensor_transform.get('y', 0), z=self.hero_vehicle.bounding_box.extent.z)

                # NOTE: 向左
                # location = carla.Location(x=0,
                #                           y=-self.hero_vehicle.bounding_box.extent.y, z=self.hero_vehicle.bounding_box.extent.z)
                # # print(self.hero_vehicle.bounding_box.extent.x,
                # #       self.hero_vehicle.bounding_box.extent.y, self.hero_vehicle.bounding_box.extent.z)
                # yaw = -90

                # pitch = -40
                # roll = -40
                # NOTE: 向右
                # location = carla.Location(x=0,
                #                           y=1.38728266954422, z=1.4936033487319946)
                # location = carla.Location(x=0,
                #                           y=self.hero_vehicle.bounding_box.extent.y, z=self.hero_vehicle.bounding_box.extent.z)
                # yaw = 90

                # pitch = -40
                # roll = -90

                # NOTE: 向后
                # location = carla.Location(x=-self.hero_vehicle.bounding_box.extent.x + 0.03,
                #                           y=sensor_transform.get('y', 0), z=self.hero_vehicle.bounding_box.extent.z)
                # yaw = 180

                # INFO
                sensor_camera_semantic_segmentation_1 = self.world.get_blueprint_library().find('sensor.camera.semantic_segmentation')
                sensor_camera_rgb_1 = self.world.get_blueprint_library().find('sensor.camera.rgb')
                sensor_camera_semantic_segmentation_2 = self.world.get_blueprint_library().find('sensor.camera.semantic_segmentation')
                sensor_camera_rgb_2 = self.world.get_blueprint_library().find('sensor.camera.rgb')
                sensor_camera_semantic_segmentation_3 = self.world.get_blueprint_library().find('sensor.camera.semantic_segmentation')
                sensor_camera_rgb_3 = self.world.get_blueprint_library().find('sensor.camera.rgb')
                sensor_camera_semantic_segmentation_4 = self.world.get_blueprint_library().find('sensor.camera.semantic_segmentation')
                sensor_camera_rgb_4 = self.world.get_blueprint_library().find('sensor.camera.rgb')
                for key, value in sensor_group['SETUP'].items():
                    sensor_camera_semantic_segmentation_1.set_attribute(key, value)
                    sensor_camera_rgb_1.set_attribute(key, value)
                    sensor_camera_semantic_segmentation_2.set_attribute(key, value)
                    sensor_camera_rgb_2.set_attribute(key, value)
                    sensor_camera_semantic_segmentation_3.set_attribute(key, value)
                    sensor_camera_rgb_3.set_attribute(key, value)
                    sensor_camera_semantic_segmentation_4.set_attribute(key, value)
                    sensor_camera_rgb_4.set_attribute(key, value)

                sensor_camera_semantic_segmentation_1.set_attribute('sensor_tick', '0.05')
                sensor_camera_rgb_1.set_attribute('sensor_tick', '0.05')
                sensor_camera_semantic_segmentation_2.set_attribute('sensor_tick', '0.05')
                sensor_camera_rgb_2.set_attribute('sensor_tick', '0.05')
                sensor_camera_semantic_segmentation_3.set_attribute('sensor_tick', '0.05')
                sensor_camera_rgb_3.set_attribute('sensor_tick', '0.05')
                sensor_camera_semantic_segmentation_4.set_attribute('sensor_tick', '0.05')
                sensor_camera_rgb_4.set_attribute('sensor_tick', '0.05')

                # INFO
                # NOTE: 向前
                location = carla.Location(x=self.hero_vehicle.bounding_box.extent.x,
                                          y=sensor_transform.get('y', 0), z=self.hero_vehicle.bounding_box.extent.z)

                transform_left = carla.Transform(location, carla.Rotation(yaw=yaw - 90, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_semantic_segmentation_1,
                             transform_left, parent=self.hero_vehicle))

                transform_right = carla.Transform(location, carla.Rotation(yaw=yaw + 90, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_semantic_segmentation_1,
                             transform_right, parent=self.hero_vehicle))

                transform_top = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch + 90, roll=roll))
                batch.append(SpawnActor(sensor_camera_semantic_segmentation_1, transform_top, parent=self.hero_vehicle))

                transform_bottom = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch - 90, roll=roll))
                batch.append(SpawnActor(sensor_camera_semantic_segmentation_1,
                             transform_bottom, parent=self.hero_vehicle))

                transform_front = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_semantic_segmentation_1,
                             transform_front, parent=self.hero_vehicle))

                transform_left = carla.Transform(location, carla.Rotation(yaw=yaw - 90, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_rgb_1, transform_left, parent=self.hero_vehicle))

                transform_right = carla.Transform(location, carla.Rotation(yaw=yaw + 90, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_rgb_1, transform_right, parent=self.hero_vehicle))

                transform_top = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch + 90, roll=roll))
                batch.append(SpawnActor(sensor_camera_rgb_1, transform_top, parent=self.hero_vehicle))

                transform_bottom = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch - 90, roll=roll))
                batch.append(SpawnActor(sensor_camera_rgb_1, transform_bottom, parent=self.hero_vehicle))

                transform_front = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_rgb_1, transform_front, parent=self.hero_vehicle))
            # INFO
                # NOTE: 向左
                location = carla.Location(x=0,
                                          y=-self.hero_vehicle.bounding_box.extent.y, z=self.hero_vehicle.bounding_box.extent.z)
                yaw = -90

                transform_left = carla.Transform(location, carla.Rotation(yaw=yaw - 90, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_semantic_segmentation_2,
                             transform_left, parent=self.hero_vehicle))

                transform_right = carla.Transform(location, carla.Rotation(yaw=yaw + 90, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_semantic_segmentation_2,
                             transform_right, parent=self.hero_vehicle))

                transform_top = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch + 90, roll=roll))
                batch.append(SpawnActor(sensor_camera_semantic_segmentation_2, transform_top, parent=self.hero_vehicle))

                transform_bottom = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch - 90, roll=roll))
                batch.append(SpawnActor(sensor_camera_semantic_segmentation_2,
                             transform_bottom, parent=self.hero_vehicle))

                transform_front = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_semantic_segmentation_2,
                             transform_front, parent=self.hero_vehicle))

                transform_left = carla.Transform(location, carla.Rotation(yaw=yaw - 90, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_rgb_2, transform_left, parent=self.hero_vehicle))

                transform_right = carla.Transform(location, carla.Rotation(yaw=yaw + 90, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_rgb_2, transform_right, parent=self.hero_vehicle))

                transform_top = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch + 90, roll=roll))
                batch.append(SpawnActor(sensor_camera_rgb_2, transform_top, parent=self.hero_vehicle))

                transform_bottom = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch - 90, roll=roll))
                batch.append(SpawnActor(sensor_camera_rgb_2, transform_bottom, parent=self.hero_vehicle))

                transform_front = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_rgb_2, transform_front, parent=self.hero_vehicle))
            # INFO
                # NOTE: 向右
                location = carla.Location(x=0,
                                          y=self.hero_vehicle.bounding_box.extent.y, z=self.hero_vehicle.bounding_box.extent.z)
                yaw = 90

                transform_left = carla.Transform(location, carla.Rotation(yaw=yaw - 90, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_semantic_segmentation_3,
                             transform_left, parent=self.hero_vehicle))

                transform_right = carla.Transform(location, carla.Rotation(yaw=yaw + 90, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_semantic_segmentation_3,
                             transform_right, parent=self.hero_vehicle))

                transform_top = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch + 90, roll=roll))
                batch.append(SpawnActor(sensor_camera_semantic_segmentation_3, transform_top, parent=self.hero_vehicle))

                transform_bottom = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch - 90, roll=roll))
                batch.append(SpawnActor(sensor_camera_semantic_segmentation_3,
                             transform_bottom, parent=self.hero_vehicle))

                transform_front = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_semantic_segmentation_3,
                             transform_front, parent=self.hero_vehicle))

                transform_left = carla.Transform(location, carla.Rotation(yaw=yaw - 90, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_rgb_3, transform_left, parent=self.hero_vehicle))

                transform_right = carla.Transform(location, carla.Rotation(yaw=yaw + 90, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_rgb_3, transform_right, parent=self.hero_vehicle))

                transform_top = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch + 90, roll=roll))
                batch.append(SpawnActor(sensor_camera_rgb_3, transform_top, parent=self.hero_vehicle))

                transform_bottom = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch - 90, roll=roll))
                batch.append(SpawnActor(sensor_camera_rgb_3, transform_bottom, parent=self.hero_vehicle))

                transform_front = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_rgb_3, transform_front, parent=self.hero_vehicle))
            # INFO
                # NOTE: 向后
                location = carla.Location(x=-self.hero_vehicle.bounding_box.extent.x + 0.03,
                                          y=sensor_transform.get('y', 0), z=self.hero_vehicle.bounding_box.extent.z)
                yaw = 180
                transform_left = carla.Transform(location, carla.Rotation(yaw=yaw - 90, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_semantic_segmentation_4,
                             transform_left, parent=self.hero_vehicle))

                transform_right = carla.Transform(location, carla.Rotation(yaw=yaw + 90, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_semantic_segmentation_4,
                             transform_right, parent=self.hero_vehicle))

                transform_top = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch + 90, roll=roll))
                batch.append(SpawnActor(sensor_camera_semantic_segmentation_4, transform_top, parent=self.hero_vehicle))

                transform_bottom = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch - 90, roll=roll))
                batch.append(SpawnActor(sensor_camera_semantic_segmentation_4,
                             transform_bottom, parent=self.hero_vehicle))

                transform_front = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_semantic_segmentation_4,
                             transform_front, parent=self.hero_vehicle))

                transform_left = carla.Transform(location, carla.Rotation(yaw=yaw - 90, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_rgb_4, transform_left, parent=self.hero_vehicle))

                transform_right = carla.Transform(location, carla.Rotation(yaw=yaw + 90, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_rgb_4, transform_right, parent=self.hero_vehicle))

                transform_top = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch + 90, roll=roll))
                batch.append(SpawnActor(sensor_camera_rgb_4, transform_top, parent=self.hero_vehicle))

                transform_bottom = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch - 90, roll=roll))
                batch.append(SpawnActor(sensor_camera_rgb_4, transform_bottom, parent=self.hero_vehicle))

                transform_front = carla.Transform(location, carla.Rotation(yaw=yaw, pitch=pitch, roll=roll))
                batch.append(SpawnActor(sensor_camera_rgb_4, transform_front, parent=self.hero_vehicle))
            # INFO
            if sensor_group["TYPE"] == "camera_fisheye":
                set_sensors_fisheye(sensor_group, batch)
                continue

            # INFO

    # TAG
        for i, response in enumerate(self.client.apply_batch_sync(batch, True)):
            if response.error:
                self.logger.info(response.error)
            else:
                actor = self.world.get_actor(response.actor_id)
                if i < 5:
                    self.sensor_actors_1.append(actor)
                elif i >= 5 and i <= 9:
                    # else:
                    self.sensor_actors_1_.append(actor)
                elif i >= 10 and i <= 14:
                    self.sensor_actors_2.append(actor)
                elif i >= 15 and i <= 19:
                    self.sensor_actors_2_.append(actor)
                elif i >= 20 and i <= 24:
                    self.sensor_actors_3.append(actor)
                elif i >= 25 and i <= 29:
                    self.sensor_actors_3_.append(actor)
                elif i >= 30 and i <= 34:
                    self.sensor_actors_4.append(actor)
                else:
                    self.sensor_actors_4_.append(actor)

                # print(len(self.sensor_actors_2_))

    # TAG
    def set_sensor_queue(self):
        for sensor in self.sensor_actors_1:
            q = queue.Queue()
            sensor.listen(q.put)
            self.sensor_queues_1.append(q)
            # print("sensor_queues", len(self.sensor_queues))
        for sensor in self.sensor_actors_1_:
            q_ = queue.Queue()
            sensor.listen(q_.put)
            self.sensor_queues_1_.append(q_)
            # print("sensor_queues_", len(self.sensor_queues_))
        # INFO
        for sensor in self.sensor_actors_2:
            q = queue.Queue()
            sensor.listen(q.put)
            self.sensor_queues_2.append(q)
            # print("sensor_queues", len(self.sensor_queues))
        for sensor in self.sensor_actors_2_:
            q_ = queue.Queue()
            sensor.listen(q_.put)
            self.sensor_queues_2_.append(q_)
            # print("sensor_queues_", len(self.sensor_queues_))
        # INFO
        for sensor in self.sensor_actors_3:
            q = queue.Queue()
            sensor.listen(q.put)
            self.sensor_queues_3.append(q)
            # print("sensor_queues", len(self.sensor_queues))
        for sensor in self.sensor_actors_3_:
            q_ = queue.Queue()
            sensor.listen(q_.put)
            self.sensor_queues_3_.append(q_)
            # print("sensor_queues_", len(self.sensor_queues_))
        # INFO
        for sensor in self.sensor_actors_4:
            q = queue.Queue()
            sensor.listen(q.put)
            self.sensor_queues_4.append(q)
            # print("sensor_queues", len(self.sensor_queues))
        for sensor in self.sensor_actors_4_:
            q_ = queue.Queue()
            sensor.listen(q_.put)
            self.sensor_queues_4_.append(q_)
            # print("sensor_queues_", len(self.sensor_queues_))
        self.logger.info('Set sensors Done!')

    def set_spectator(self, z=20, pitch=-90):
        spectator = self.world.get_spectator()
        hero_transform = self.hero_vehicle.get_transform()
        spectator.set_transform(carla.Transform(hero_transform.location+carla.Location(z=z),
                                carla.Rotation(yaw=hero_transform.rotation.yaw, pitch=pitch, roll=hero_transform.rotation.roll)))

    def is_bug_vehicle(self, vehicle):
        if vehicle.bounding_box.extent.x == 0.0 or vehicle.bounding_box.extent.y == 0.0:
            return True
        return False

    def is_bug_pedestrian(pedestrian):
        if pedestrian.bounding_box.extent.x == 0.0 or pedestrian.bounding_box.extent.y == 0.0:
            return True
        return False

    def is_cyclist(self, vehicle):
        if vehicle.attributes['number_of_wheels'] == '2':
            return True
        return False

    def filter_vehicles_dont_want(self):
        self.logger.info(f'num of environment vehicles before filtering: {len(self.env_vehicles)}')

        DestroyActor = carla.command.DestroyActor
        destroyed_list = []
        batch = []

        for env_vehicle in self.env_vehicles:
            if self.is_bug_vehicle(env_vehicle):
                batch.append(DestroyActor(env_vehicle))
                destroyed_list.append(env_vehicle)

        for env_vehicle in destroyed_list:
            self.env_vehicles.remove(env_vehicle)

        self.client.apply_batch_sync(batch, True)
        self.logger.info(f'num of environment vehicles after filtering: {len(self.env_vehicles)}')

    def filter_pedestrians_dont_want(self):
        destroyed_list = []
        batch = []

        for pedestrian in self.pedestrians:
            if self.is_bug_pedestrian(pedestrian):
                batch.append(carla.command.DestroyActor(pedestrian))
                destroyed_list.append(pedestrian)

        for pedestrian in destroyed_list:
            self.pedestrians.remove(pedestrian)

        self.client.apply_batch_sync(batch, True)
        self.logger.info(f'num of environment vehipedestrianscles after filtering: {len(self.env_vehicles)}')

        return self.pedestrians

    # TAG
    def process_semantic(self, image):
        # image.convert(carla.ColorConverter.CityScapesPalette)
        image.convert(carla.ColorConverter.Raw)
        # array = np.frombuffer(image.raw_data, dtype=np.dtype("uint8"))
        # array = np.reshape(array, (image.height, image.width, 4))
        # array = array[:, :, :3]
        return image

    # TAG
    def retrieve_data(self, sensor_queue, timeout=10.0):
        while True:
            data_origin = sensor_queue.get(timeout=timeout)
            if data_origin.frame == self.frame:
                # print(data_origin)
                # print("process_semantic",process_semantic(data_origin))
                return self.process_semantic(data_origin)

    # TAG
    def retrieve_data_(self, sensor_queue, timeout=10.0):
        while True:
            data_origin = sensor_queue.get(timeout=timeout)
            if data_origin.frame == self.frame:
                # print("data_origin",data_origin)
                return data_origin

    def destroy_actors(self):
        self.hero_vehicle.destroy()
        for actor in self.env_vehicles:
            actor.destroy()
        for actor in self.sensor_actors_1:
            actor.destroy()
        for actor in self.sensor_actors_1_:
            actor.destroy()
        for actor in self.sensor_actors_2:
            actor.destroy()
        for actor in self.sensor_actors_2_:
            actor.destroy()
        for actor in self.sensor_actors_3:
            actor.destroy()
        for actor in self.sensor_actors_3_:
            actor.destroy()
        for actor in self.sensor_actors_4:
            actor.destroy()
        for actor in self.sensor_actors_4_:
            actor.destroy()

    def start_collecting(self):
        flag = False
        self.client = carla.Client(CLIENT_HOST, CLIENT_PORT)
        self.client.set_timeout(50.0)

        self.world = self.client.load_world(self.map)
        self.world.unload_map_layer(carla.MapLayer.ParkedVehicles)  # remove parked vehicles

        traffic_manager = self.client.get_trafficmanager(TRAFFIC_MANAGER_PORT)

        try:
            self.logger.info('------------------------ Start Generating ------------------------')

            self.set_hero_vehicle()

            # self.set_env_vehicles()
            # self.filter_vehicles_dont_want()
            # self.set_env_pedestrians()

            # self.filter_pedestrians_dont_want()
            # print("success1")
            self.set_sensors()
            self.set_sensor_queue()

            # generate_traffic.main()
            self.set_traffic_lights_to_green()
            self.set_synchronization_world()
            self.set_synchronization_traffic_manager(traffic_manager)

            time_stamp = self.start_timestamp
            interval_index = 0

            while time_stamp < self.total_timestamp + self.start_timestamp:
                self.frame = self.world.tick()

                self.set_spectator(z=5, pitch=-30)  # set spectator for visualization

                ############################ Get Data ##################################

                # data_total = [self.retrieve_data(q) for q in self.sensor_queues]
                # data_total_ = [self.retrieve_data_(q_) for q_ in self.sensor_queues_]
                data_total_1 = [self.retrieve_data(q) for q in self.sensor_queues_1]
                data_total_1_ = [self.retrieve_data_(q_) for q_ in self.sensor_queues_1_]
                data_total_2 = [self.retrieve_data(q) for q in self.sensor_queues_2]
                data_total_2_ = [self.retrieve_data_(q_) for q_ in self.sensor_queues_2_]
                data_total_3 = [self.retrieve_data(q) for q in self.sensor_queues_3]
                data_total_3_ = [self.retrieve_data_(q_) for q_ in self.sensor_queues_3_]
                data_total_4 = [self.retrieve_data(q) for q in self.sensor_queues_4]
                data_total_4_ = [self.retrieve_data_(q_) for q_ in self.sensor_queues_4_]
                # print("data_total_2_", data_total_2_)
                ########################## Check Save Interval ########################
                # NOTE: 跳帧
                if flag == False and self.initialize_nums <= 10:
                    self.initialize_nums += 1
                    continue

                if self.save_interval != None and (interval_index + 1) != self.save_interval and flag == True:
                    interval_index += 1
                    if interval_index % 20 == 0:
                        print(interval_index, end=" ", flush=True)
                    continue

                print('20\n')
                interval_index = 0

                ############################# Save Data ###########################
                reference_sensor_transform = None
                for sensor_group in self.sensor_group_list:
                    save_path = os.path.join(self.data_save_path, sensor_group["NAME"])

                    if sensor_group["TYPE"] == 'camera_fisheye':
                        num_cameras = 5
                        # print(len(data_total))
                        # data_group = data_total[:num_cameras]
                        # data_total = data_total[num_cameras:]
                        # data_group_ = data_total_[:num_cameras]
                        # data_total_ = data_total_[num_cameras:]

                        data_group_1 = data_total_1[:num_cameras]
                        data_total_1 = data_total_1[num_cameras:]
                        data_group_1_ = data_total_1_[:num_cameras]
                        data_total_1_ = data_total_1_[num_cameras:]

                        data_group_2 = data_total_2[:num_cameras]
                        data_total_2 = data_total_2[num_cameras:]
                        data_group_2_ = data_total_2_[:num_cameras]
                        data_total_2_ = data_total_2_[num_cameras:]

                        data_group_3 = data_total_3[:num_cameras]
                        data_total_3 = data_total_3[num_cameras:]
                        data_group_3_ = data_total_3_[:num_cameras]
                        data_total_3_ = data_total_3_[num_cameras:]

                        data_group_4 = data_total_4[:num_cameras]
                        data_total_4 = data_total_4[num_cameras:]
                        data_group_4_ = data_total_4_[:num_cameras]
                        data_total_4_ = data_total_4_[num_cameras:]

                        PicSize = sensor_group["PicSize"]
                        FishSize = sensor_group["FishSize"]
                        FOV = sensor_group["FOV"]

                        # TAG
                        # for data in data_group:
                        #    print("111111111",dir(data))
                        # cv2.imwrite("/home/m0rtzz/%06d.png", "%06d.png" % (time_stamp), picture_group)
                        # picture_group[0] = cv2.cvtColor(picture_group[0], cv2.COLOR_BGR2RGB)
                        # cv2.imwrite(os.path.join("/home/m0rtzz/", "%06d.png" %
                        #             (time_stamp)), picture_group[0])

                        # TAG
                        # for data in data_group_:
                        #     print("22222222",dir(data))
                        # picture_group = picture_group_
                        # INFO
                        # fisheye_picture = cv2.normalize(fisheye_picture, None, 0, 255,
                        #                                 cv2.NORM_MINMAX, dtype=cv2.CV_64F)

                        # fisheye_picture = cv2.cvtColor(fisheye_picture, cv2.COLOR_BGR2RGB)
                        # gray_image = cv2.cvtColor(fisheye_picture, cv2.COLOR_BGR2GRAY)

                        # save_path = "/home/m0rtzz/Program_Files/carla-0.9.13/PythonAPI/examples/carla-data-generator/data/fisheye/semantic_segmentation_raw/"
                        # file_name = "%06d.png" % time_stamp
                        # file_name_with_suffix = file_name.split(".")[0] + "_Raw.png"
                        # file_path = os.path.join(save_path, file_name_with_suffix)
                        # gray_image = cv2.flip(gray_image, 1)
                        # # NOTE: 这样是正确的调色板分割图像
                        # # gray_image = cv2.cvtColor(gray_image, cv2.COLOR_BGR2RGB)

                        # # TODO: 试一下像素值对不对
                        # gray_image = cv2.cvtColor(gray_image, cv2.COLOR_BGR2GRAY)
                        # red_channel = cv2.flip(red_channel, 1)
                        # # cv2.imwrite(file_path, gray_image)
                        # cv2.imwrite(file_path, red_channel)

                        # cv2.imwrite(os.path.join(save_path, "%06d__.png" % (time_stamp)), fisheye_picture_)
                        # save_path = "/home/m0rtzz/Program_Files/carla-0.9.13/PythonAPI/examples/carla-data-generator/data/fisheye/rgb/"
                        # file_name = "%06d.png" % time_stamp
                        # file_name_with_suffix = file_name.split(".")[0] + "_RGB.png"
                        # file_path = os.path.join(save_path, file_name_with_suffix)
                        # fisheye_picture_ = cv2.flip(fisheye_picture_, 1)
                        # cv2.imwrite(file_path, fisheye_picture_)
                        # INFO
                        # NOTE: 向前
                        picture_group_1 = [np.reshape(np.frombuffer(data.raw_data, dtype=np.dtype("uint8")), (PicSize, PicSize, 4))[
                            :, :, :3][:, :, ::-1] for data in data_group_1]
                        picture_group_1_ = [np.reshape(np.frombuffer(data.raw_data, dtype=np.dtype("uint8")), (PicSize, PicSize, 4))[
                            :, :, :3][:, :, ::-1] for data in data_group_1_]

                        # output_folder = "/home/m0rtzz/Program_Files/carla-0.9.14/_out/"

                        # existing_files = os.listdir(output_folder)
                        # num_existing_files = len(existing_files)

                        # for i, x in enumerate(data_group_1):
                        #     y = np.reshape(np.frombuffer(x.raw_data, dtype=np.dtype("uint8")), (PicSize, PicSize, 4))
                        #     file_name = "{:06d}.png".format(num_existing_files + i)
                        #     save_path = os.path.join(output_folder, file_name)
                        #     red_channel = y[:, :, 0]
                        #     cv2.imwrite(save_path, red_channel)

                        # for i, x in enumerate(data_group_1_):
                        #     y = np.reshape(np.frombuffer(x.raw_data, dtype=np.dtype("uint8")), (PicSize, PicSize, 4))
                        #     file_name = "{:06d}_.png".format(num_existing_files + i)
                        #     save_path = os.path.join(output_folder, file_name)
                        #     cv2.imwrite(save_path, y)

                        # NOTE: 语义分割原始图像
                        fisheye_picture = fisheye_utils.cube2fisheye(picture_group_1, PicSize, FishSize, FOV)
                        fisheye_picture = fisheye_picture.astype(np.uint8)
                        red_channel = fisheye_picture[:, :, 0]
                        gray_image = fisheye_picture

                        save_path = "./images/my_images/fisheye_dataset/semantic_segmentation_raw/"
                        file_names = os.listdir(save_path)

                        front_files = [f for f in file_names if "FRONT" in f]
                        latest_front_semantic_segmentation_file_name = sorted(front_files)[-1] if front_files else None
                        latest_front_semantic_segmentation_number = int(latest_front_semantic_segmentation_file_name.split("_")[
                            0]) if latest_front_semantic_segmentation_file_name else -1

                        new_front_number = latest_front_semantic_segmentation_number + 1

                        new_front_semantic_segmentation_file_name = "{:06d}_FRONT.png".format(new_front_number)
                        new_front_semantic_segmentation_file_path = os.path.join(
                            save_path, new_front_semantic_segmentation_file_name)

                        gray_image = cv2.flip(gray_image, 1)
                        gray_image = cv2.cvtColor(gray_image, cv2.COLOR_BGR2GRAY)
                        red_channel = cv2.flip(red_channel, 1)

                        cv2.imwrite(new_front_semantic_segmentation_file_path, red_channel)
                        self.logger.info("RAW: %s \033[32m%s\033[0m",
                                         new_front_semantic_segmentation_file_name, "saved successfully!")

                        # NOTE: RGB图像
                        fisheye_picture_ = fisheye_utils.cube2fisheye(picture_group_1_, PicSize, FishSize, FOV)
                        fisheye_picture_ = fisheye_picture_.astype(np.uint8)
                        fisheye_picture_ = cv2.cvtColor(fisheye_picture_, cv2.COLOR_BGR2RGB)
                        save_path = "./images/my_images/fisheye_dataset/rgb/"
                        file_names = os.listdir(save_path)

                        front_files = [f for f in file_names if "FRONT" in f]
                        latest_front_rgb_file_name = sorted(front_files)[-1] if front_files else None
                        latest_front_rgb_number = int(latest_front_rgb_file_name.split("_")[
                                                      0]) if latest_front_rgb_file_name else -1

                        new_front_rgb_number = latest_front_rgb_number + 1
                        new_front_rgb_file_name = "{:06d}_FRONT.png".format(new_front_rgb_number)
                        new_front_rgb_file_path = os.path.join(save_path, new_front_rgb_file_name)

                        fisheye_picture_ = cv2.flip(fisheye_picture_, 1)
                        cv2.imwrite(new_front_rgb_file_path, fisheye_picture_)
                        self.logger.info("RGB: %s \033[32m%s\033[0m", new_front_rgb_file_name, "saved successfully!")
                        # INFO
                        # NOTE: 向左
                        picture_group_2 = [np.reshape(np.frombuffer(data.raw_data, dtype=np.dtype("uint8")), (PicSize, PicSize, 4))[
                            :, :, :3][:, :, ::-1] for data in data_group_2]
                        picture_group_2_ = [np.reshape(np.frombuffer(data.raw_data, dtype=np.dtype("uint8")), (PicSize, PicSize, 4))[
                            :, :, :3][:, :, ::-1] for data in data_group_2_]
                        # NOTE: 语义分割原始图像
                        fisheye_picture = fisheye_utils.cube2fisheye(picture_group_2, PicSize, FishSize, FOV)
                        fisheye_picture = fisheye_picture.astype(np.uint8)
                        red_channel = fisheye_picture[:, :, 0]
                        gray_image = fisheye_picture

                        save_path = "./images/my_images/fisheye_dataset/semantic_segmentation_raw/"
                        file_names = os.listdir(save_path)

                        left_files = [f for f in file_names if "LEFT" in f]
                        latest_left_semantic_segmentation_file_name = sorted(left_files)[-1] if left_files else None
                        latest_left_semantic_segmentation_number = int(latest_left_semantic_segmentation_file_name.split("_")[
                                                                       0]) if latest_left_semantic_segmentation_file_name else -1

                        new_left_semantic_segmentation_number = latest_left_semantic_segmentation_number + 1

                        new_left_semantic_segmentation_file_name = "{:06d}_LEFT.png".format(
                            new_left_semantic_segmentation_number)
                        new_left_semantic_segmentation_file_path = os.path.join(
                            save_path, new_left_semantic_segmentation_file_name)

                        gray_image = cv2.flip(gray_image, 1)
                        gray_image = cv2.cvtColor(gray_image, cv2.COLOR_BGR2GRAY)
                        red_channel = cv2.flip(red_channel, 1)

                        cv2.imwrite(new_left_semantic_segmentation_file_path, red_channel)
                        self.logger.info("RAW: %s \033[32m%s\033[0m",
                                         new_left_semantic_segmentation_file_name, "saved successfully!")

                        # NOTE: RGB图像
                        fisheye_picture_ = fisheye_utils.cube2fisheye(picture_group_2_, PicSize, FishSize, FOV)
                        fisheye_picture_ = fisheye_picture_.astype(np.uint8)
                        fisheye_picture_ = cv2.cvtColor(fisheye_picture_, cv2.COLOR_BGR2RGB)
                        save_path = "./images/my_images/fisheye_dataset/rgb/"
                        file_names = os.listdir(save_path)

                        left_files = [f for f in file_names if "LEFT" in f]
                        latest_left_rgb_file_name = sorted(left_files)[-1] if left_files else None
                        latest_left_rgb_number = int(latest_left_rgb_file_name.split("_")[
                                                     0]) if latest_left_rgb_file_name else -1

                        new_left_rgb_number = latest_left_rgb_number + 1
                        new_left_rgb_file_name = "{:06d}_LEFT.png".format(new_left_rgb_number)
                        new_left_rgb_file_path = os.path.join(save_path, new_left_rgb_file_name)

                        fisheye_picture_ = cv2.flip(fisheye_picture_, 1)
                        cv2.imwrite(new_left_rgb_file_path, fisheye_picture_)
                        self.logger.info("RGB: %s \033[32m%s\033[0m", new_left_rgb_file_name, "saved successfully!")
                        # INFO
                        # NOTE: 向右
                        picture_group_3 = [np.reshape(np.frombuffer(data.raw_data, dtype=np.dtype("uint8")), (PicSize, PicSize, 4))[
                            :, :, :3][:, :, ::-1] for data in data_group_3]
                        picture_group_3_ = [np.reshape(np.frombuffer(data.raw_data, dtype=np.dtype("uint8")), (PicSize, PicSize, 4))[
                            :, :, :3][:, :, ::-1] for data in data_group_3_]
                        # NOTE: 语义分割原始图像
                        fisheye_picture = fisheye_utils.cube2fisheye(picture_group_3, PicSize, FishSize, FOV)
                        fisheye_picture = fisheye_picture.astype(np.uint8)
                        red_channel = fisheye_picture[:, :, 0]
                        gray_image = fisheye_picture

                        save_path = "./images/my_images/fisheye_dataset/semantic_segmentation_raw/"
                        file_names = os.listdir(save_path)

                        right_files = [f for f in file_names if "RIGHT" in f]
                        latest_right_semantic_segmentation_file_name = sorted(right_files)[-1] if right_files else None
                        latest_right_semantic_segmentation_number = int(latest_right_semantic_segmentation_file_name.split("_")[
                            0]) if latest_right_semantic_segmentation_file_name else -1

                        new_right_semantic_segmentation_number = latest_right_semantic_segmentation_number + 1

                        new_right_semantic_segmentation_file_name = "{:06d}_RIGHT.png".format(
                            new_right_semantic_segmentation_number)
                        new_right_semantic_segmentation_file_path = os.path.join(
                            save_path, new_right_semantic_segmentation_file_name)

                        gray_image = cv2.flip(gray_image, 1)
                        gray_image = cv2.cvtColor(gray_image, cv2.COLOR_BGR2GRAY)
                        red_channel = cv2.flip(red_channel, 1)

                        cv2.imwrite(new_right_semantic_segmentation_file_path, red_channel)
                        self.logger.info("RAW: %s \033[32m%s\033[0m",
                                         new_right_semantic_segmentation_file_name, "saved successfully!")

                        # NOTE: RGB图像
                        fisheye_picture_ = fisheye_utils.cube2fisheye(picture_group_3_, PicSize, FishSize, FOV)
                        fisheye_picture_ = fisheye_picture_.astype(np.uint8)
                        fisheye_picture_ = cv2.cvtColor(fisheye_picture_, cv2.COLOR_BGR2RGB)

                        save_path = "./images/my_images/fisheye_dataset/rgb/"
                        file_names = os.listdir(save_path)

                        right_files = [f for f in file_names if "RIGHT" in f]
                        latest_right_rgb_file_name = sorted(right_files)[-1] if right_files else None
                        latest_right_rgb_number = int(latest_right_rgb_file_name.split("_")[
                                                      0]) if latest_right_rgb_file_name else -1

                        new_right_rgb_number = latest_right_rgb_number + 1
                        new_right_rgb_file_name = "{:06d}_RIGHT.png".format(new_right_rgb_number)
                        new_right_rgb_file_path = os.path.join(save_path, new_right_rgb_file_name)

                        fisheye_picture_ = cv2.flip(fisheye_picture_, 1)
                        cv2.imwrite(new_right_rgb_file_path, fisheye_picture_)
                        self.logger.info("RGB: %s \033[32m%s\033[0m", new_right_rgb_file_name, "saved successfully!")
                        # INFO
                        # NOTE: 向后
                        picture_group_4 = [np.reshape(np.frombuffer(data.raw_data, dtype=np.dtype("uint8")), (PicSize, PicSize, 4))[
                            :, :, :3][:, :, ::-1] for data in data_group_4]
                        picture_group_4_ = [np.reshape(np.frombuffer(data.raw_data, dtype=np.dtype("uint8")), (PicSize, PicSize, 4))[
                            :, :, :3][:, :, ::-1] for data in data_group_4_]
                        # NOTE: 语义分割原始图像
                        fisheye_picture = fisheye_utils.cube2fisheye(picture_group_4, PicSize, FishSize, FOV)
                        fisheye_picture = fisheye_picture.astype(np.uint8)
                        red_channel = fisheye_picture[:, :, 0]
                        gray_image = fisheye_picture

                        save_path = "./images/my_images/fisheye_dataset/semantic_segmentation_raw/"
                        file_names = os.listdir(save_path)

                        rear_files = [f for f in file_names if "REAR" in f]
                        latest_rear_semantic_segmentation_file_name = sorted(rear_files)[-1] if rear_files else None
                        latest_rear_semantic_segmentation_number = int(latest_rear_semantic_segmentation_file_name.split("_")[
                            0]) if latest_rear_semantic_segmentation_file_name else -1

                        new_rear_semantic_segmentation_number = latest_rear_semantic_segmentation_number + 1

                        new_rear_semantic_segmentation_file_name = "{:06d}_REAR.png".format(
                            new_rear_semantic_segmentation_number)
                        new_rear_semantic_segmentation_file_path = os.path.join(
                            save_path, new_rear_semantic_segmentation_file_name)

                        gray_image = cv2.flip(gray_image, 1)
                        gray_image = cv2.cvtColor(gray_image, cv2.COLOR_BGR2GRAY)
                        red_channel = cv2.flip(red_channel, 1)

                        cv2.imwrite(new_rear_semantic_segmentation_file_path, red_channel)
                        self.logger.info("RAW: %s \033[32m%s\033[0m",
                                         new_rear_semantic_segmentation_file_name, "saved successfully!")

                        # NOTE: RGB图像
                        fisheye_picture_ = fisheye_utils.cube2fisheye(picture_group_4_, PicSize, FishSize, FOV)
                        fisheye_picture_ = fisheye_picture_.astype(np.uint8)
                        fisheye_picture_ = cv2.cvtColor(fisheye_picture_, cv2.COLOR_BGR2RGB)

                        save_path = "./images/my_images/fisheye_dataset/rgb/"
                        file_names = os.listdir(save_path)
                        rear_files = [f for f in file_names if "REAR" in f]
                        latest_rear_rgb_file_name = sorted(rear_files)[-1] if rear_files else None
                        latest_rear_rgb_number = int(latest_rear_rgb_file_name.split("_")[
                            0]) if latest_rear_rgb_file_name else -1

                        new_rear_rgb_number = latest_rear_rgb_number + 1
                        new_rear_rgb_file_name = "{:06d}_REAR.png".format(new_rear_rgb_number)
                        new_rear_rgb_file_path = os.path.join(save_path, new_rear_rgb_file_name)
                        fisheye_picture_ = cv2.flip(fisheye_picture_, 1)
                        cv2.imwrite(new_rear_rgb_file_path, fisheye_picture_)
                        self.logger.info("RGB: %s \033[32m%s\033[0m", new_rear_rgb_file_name, "saved successfully!")
                        # INFO
                        # TAG
                        # cc = .
                        # for data in data_group:
                        #     print(data)

                # self.logger.info(f'Time stamp {time_stamp} saved successfully!')
                flag = True
                self.logger.info(f'Time stamp {time_stamp} \033[32msaved successfully!\033[0m\n')
                print("\ninterval_index: ", flush=True)

                # print("\n")
                time_stamp += 1

        except RuntimeError:
            self.logger.info('Something wrong happened!')

        except KeyboardInterrupt:
            self.logger.info('Exit by user!')

        finally:
            self.set_synchronization_world(synchronous_mode=False)
            self.logger.info('------------------- Destroying actors -----------------')
            self.destroy_actors()
            self.logger.info('------------------------ Done ------------------------')

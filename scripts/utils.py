import yaml
import logging 
import datetime
import os
import numpy as np

def config_from_yaml(config_file):
    if config_file == None:
        raise RuntimeError
    with open(config_file, 'r') as f:
        collector_config = yaml.safe_load(f)
    return collector_config

def create_logger(log_dir='log'):
    log_file = 'log_generator_%s.txt' % datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    log_file = os.path.join(log_dir, log_file)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s  %(levelname)5s  %(message)s')

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    logger.addHandler(console)

    file_handler = logging.FileHandler(filename=log_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.propagate = False

    return logger

def transform_points_to_reference(point, local_transform, reference_transform):
    cords = point[:, :4].copy()
    cords[:, -1] = 1
    local_sensor_to_world = local_transform.get_matrix()
    world_to_reference_sensor = reference_transform.get_inverse_matrix()
    cords = np.dot(np.dot(world_to_reference_sensor, local_sensor_to_world), cords.T).T
    point[:, :3] = cords[:, :3]
    point[:, 1] = - point[:, 1]
    return point

def actor2type(actor):
    CYCLIST = ['vehicle.bh.crossbike',
                'vehicle.diamondback.century',
                'vehicle.harley-davidson.low_rider',
                'vehicle.gazelle.omafiets',
                'vehicle.kawasaki.ninja',
                'vehicle.yamaha.yzf']
    if actor.type_id.startswith('walker'):
        return 'Pedestrian'
    elif actor.bounding_box.extent.x >= 4:
        return 'Truck'
    elif actor.type_id in CYCLIST:
        return 'Cyclist'
    else:
        return 'Car'

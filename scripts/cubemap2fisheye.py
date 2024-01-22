#!/home/m0rtzz/Program_Files/anaconda3/envs/py38/bin/python3

import numpy as np
import math
import os
import datetime
import cv2
import argparse


def get_spherical_coordinates(FishSize):
    """
    基于输出图像的尺寸，确定输出图像上每个点的极坐标(r, phi)
    Finds spherical coordinates on the output image
    :param output_height: height of output image
    :param output_width: width of output image
    :return: two matrices that contain spherical coordinates
    for all pixels of the output image
    """
    center = int(FishSize/2)
    cc = (center, center)

    y = np.arange(0, FishSize, 1)  # 返回一个有终点和起点的固定步长的排列（等差数组）
    x = np.arange(0, FishSize, 1)

    xx, yy = np.meshgrid(y, x)  # 将y、x中每个数据排列组合生成多个点，将各个点的x坐标放入xx中，y坐标放入yy中

    bias = np.ones((FishSize, FishSize))*cc[0]  # 生成元素全为cc[0]的矩阵

    xx = np.subtract(xx, bias)  # 将横坐标范围从0~output_height变为+-output_height/2
    yy = np.subtract(yy, bias)
    xx = np.divide(xx, bias)     # 横纵坐标标准化
    xx[:, -1] = 1
    yy = np.divide(yy, -bias)
    yy[-1, :] = -1

    r = np.sqrt(xx**2 + yy**2)  # 每个点的极坐标距离，并消除距离大于1的点
    r[r > 1] = np.nan
    r[r < 0] = 0

    phi = np.zeros((FishSize, FishSize))   # 计算每个点的极坐标角度
    phi[:center, center:] = np.arcsin(np.divide(yy[:center, center:], r[:center, center:]))
    phi[:, :center] = np.pi - np.arcsin(np.divide(yy[:, :center], r[:, :center]))
    phi[center+1:, center:] = 2*np.pi + np.arcsin(np.divide(yy[center+1:, center:], r[center+1:, center:]))
    phi[cc[0], cc[1]] = 0

    return r, phi


def spherical_to_cartesian(r, phi, fov):
    """
    Transforms spherical coordinates to cartesian
    :param r: matrix with computed pixel heights
    :param phi: matrix with computed pixel angles
    :param fov: desired field of view
    :return: x,y,z cartesian coordinates
    """
    theta = r*fov/2
    x = np.sin(theta)*np.cos(phi)
    y = np.sin(theta)*np.sin(phi)
    z = np.cos(theta)

    return x, y, z


def get_face(x, y, z):
    """
    根据三维笛卡尔坐标，确定该点位于立方体哪个表面上
    Finds which face of a cube map a 3D vector with origin
    at the center of the cube points to
    :param x, y, z: cartesian coordinates
    :return: string that indicates the face
    """

    max_axis = max(abs(x), abs(y), abs(z))

    if math.isclose(max_axis, abs(x)):  # math.isclose 两个数是否绝对/相对接近
        return 'right' if x < 0 else 'left'
    elif math.isclose(max_axis, abs(y)):
        return 'bottom' if y < 0 else 'top'
    elif math.isclose(max_axis, abs(z)):
        return 'back' if z < 0 else 'front'


def raw_face_coordinates(face, x, y, z):
    """
    Finds u,v coordinates (image coordinates) for a given
    3D vector
    :param face: face where the vector points to
    :param x, y, z: vector cartesian coordinates
    :return: uv image coordinates
    """
    if face == 'left':
        u = z
        v = -y
        ma = abs(x)
    elif face == 'right':
        u = -z
        v = -y
        ma = abs(x)
    elif face == 'bottom':
        u = -x
        v = -z
        ma = abs(y)
    elif face == 'top':
        u = -x
        v = z
        ma = abs(y)
    elif face == 'back':
        u = x
        v = y
        ma = abs(z)
    elif face == 'front':
        u = -x
        v = -y
        ma = abs(z)
    else:
        raise Exception('Tile ' + face + 'does not exist')

    return (u/ma + 1)/2, (v/ma + 1)/2


def normalized_coordinates(face, x, y, PicSize):
    """
    Finds coordinates on the 2D cube map image of a 3D
    vector
    :param face: face where a 3D vector points to
    :param x, y: image coordinates
    :param n: tiles size
    :return: coordinates on the 2D cube map image
    """
    # 首先获取该表面的原点坐标
    face_origin = {
        'left': (0, PicSize),
        'front': (PicSize, PicSize),
        'right': (2*PicSize, PicSize),
        'back': (3*PicSize, PicSize),
        'top': (PicSize, 0),
        'bottom': (PicSize, 2*PicSize),
    }
    tile_origin_coords = face_origin.get(face)

    tile_x = math.floor(x*PicSize)    # math.floor 向下取整函数
    tile_y = math.floor(y*PicSize)

    if tile_x < 0:
        tile_x = 0
    elif tile_x >= PicSize:
        tile_x = PicSize-1
    if tile_y < 0:
        tile_y = 0
    elif tile_y >= PicSize:
        tile_y = PicSize-1

    x_cubemap = tile_origin_coords[0] + tile_x
    y_cubemap = tile_origin_coords[1] + tile_y

    return x_cubemap, y_cubemap


def cube2fisheye(picture_group, PicSize, FishSize, FOV):
    lPic, rPic, tPic, bPic, fPic = picture_group
    cubemap = np.zeros((3*PicSize, 3*PicSize, 3))
    cubemap[PicSize:2*PicSize, 0:PicSize] = lPic
    cubemap[PicSize:2*PicSize, PicSize:2*PicSize] = fPic
    cubemap[PicSize:2*PicSize, 2*PicSize:3*PicSize] = rPic
    cubemap[0:PicSize, PicSize:2*PicSize] = tPic
    cubemap[2*PicSize:3*PicSize, PicSize:2*PicSize] = bPic

    fisheye_picture = np.zeros((FishSize, FishSize, 3))
    fov = FOV*np.pi/180
    r, phi = get_spherical_coordinates(FishSize)
    x, y, z = spherical_to_cartesian(r, phi, fov)

    for row in range(0, FishSize):
        for column in range(0, FishSize):
            if np.isnan(r[row, column]):    # 将输出图像平面上极坐标距离超过1的点设置为黑色
                fisheye_picture[row, column, :] = 0
            # 对于极坐标距离在1以内的点
            else:
                # 首先确定该点对应的三维坐标指向哪个立方体表面
                face = get_face(x[row, column],
                                y[row, column],
                                z[row, column])
                # 然后确定该点在该立方体表面上的uv坐标
                u, v = raw_face_coordinates(face,
                                            x[row, column],
                                            y[row, column],
                                            z[row, column])
                # 最后获取标准化的uv坐标，锁定输出图像上坐标为(row,column)的点对应着立方体哪个表面上的哪个点
                x_cubemap, y_cubemap = normalized_coordinates(face,
                                                              u,
                                                              v,
                                                              PicSize)
                # 将原图像素色彩值转移到输出图像上
                fisheye_picture[row, column, :] = cubemap[y_cubemap, x_cubemap, :]

    return fisheye_picture


def main(input_images):
    PicSize = 1024  # 立方体贴图每个面的尺寸
    FishSize = 1344  # 鱼眼图像尺寸
    FOV = 196  # 鱼眼视角
    output_path = './images/my_images/fisheye_transformation/cubemap2fisheye/'
    output_file_name = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S') + ".png"
    # 加载输入图像
    input_images = sorted(input_images, key=lambda x: (
        'LEFT' in x, 'RIGHT' in x, 'TOP' in x, 'BOTTOM' in x, 'FRONT' in x), reverse=True)
    print(input_images)
    lPic = cv2.imread(input_images[0])
    rPic = cv2.imread(input_images[1])
    tPic = cv2.imread(input_images[2])
    bPic = cv2.imread(input_images[3])
    fPic = cv2.imread(input_images[4])
    # 生成鱼眼图像
    fisheye_picture = cube2fisheye([lPic, rPic, tPic, bPic, fPic], PicSize, FishSize, FOV)

    # 保存鱼眼图像
    cv2.imwrite(output_path + output_file_name, fisheye_picture)
    if os.path.exists(output_path + output_file_name):
        print("转换成功")
        cv2.namedWindow("Press ESC to exit", cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_NORMAL)
        cv2.resizeWindow("Press ESC to exit", 800, 600)  # 设置窗口大小为 800x600
        mat = cv2.imread(output_path + output_file_name)
        cv2.imshow("Press ESC to exit", mat)
        while True:
            if cv2.waitKey(1) == 27:  # 按下esc键的ASCII码为27
                break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate fisheye image from cube map')
    parser.add_argument('input_images', type=str, nargs=5, help='input cube map images')

    args = parser.parse_args()
    main(args.input_images)

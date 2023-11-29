#!/home/m0rtzz/Program_Files/anaconda3/envs/py38/bin/python3

"""
File: m0rtzz_fisheye.py
Author: M0rtzz
Create Date: 2023-10-20
Version: 1.0
Description: origin2fisheye.
"""


import math
import numpy as np
import cv2
from tqdm import tqdm
import os


def changePoints(xd, yd, xc, yc, f):
    x = xd - xc
    y = yd - yc
    rc = (x * x + y * y) ** 0.5
    if rc == 0 or f == 0:
        st = 0
    else:
        st = math.atan(rc / f)
    rf = f * st
    if rc == 0:
        x_ = 0
        y_ = 0
    else:
        x_ = rf * x / rc
        y_ = rf * y / rc
    xx = int(x_ + xc)
    yy = int(y_ + yc)

    return xx, yy


def getOneFisheye(img, pointx, pointy, rate=0.73):
    height, width, _ = img.shape
    result = np.zeros((height, width, 3), dtype=np.uint8)
    xc = pointx + width // 2
    yc = pointy + height // 2
    f = 159
    for dy in range(height):
        for dx in range(width):
            x = pointx + dx
            y = pointy + dy
            xx, yy = changePoints(x, y, xc, yc, f)
            xx -= pointx
            yy -= pointy
            result[yy, xx] = img[y, x]

    return result


def processImages(source_dir, target_dir, keyword):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    image_files = [file for file in os.listdir(source_dir) if keyword in file]

    for image_file in tqdm(image_files):
        img_path = os.path.join(source_dir, image_file)
        target_path = os.path.join(target_dir, image_file)

        # 检查目标文件夹中是否已经存在目标文件
        if os.path.exists(target_path):
            # print("image exists")
            continue

        img = cv2.imread(img_path)

        # shape = img.shape

        result = getOneFisheye(img, 0, 0)
        # result = result[274:850, 704:1344]  # 裁剪成正方形

        cv2.imwrite(target_path, result)


if __name__ == "__main__":
    # source_dir_1 = "/home/m0rtzz/Workspaces/wmx_workspace/data/cityscapes/gtFine/train"
    # target_dir_1 = "/home/m0rtzz/Workspaces/wmx_workspace/data/cityscapes_fisheye/gtFine/train"

    # source_dir_2 = "/home/m0rtzz/Workspaces/wmx_workspace/data/cityscapes/gtFine/val"
    # target_dir_2 = "/home/m0rtzz/Workspaces/wmx_workspace/data/cityscapes_fisheye/gtFine/val"

    # source_dir_3 = "/home/m0rtzz/Workspaces/wmx_workspace/data/cityscapes/leftImg8bit/train"
    # target_dir_3 = "/home/m0rtzz/Workspaces/wmx_workspace/data/cityscapes_fisheye/leftImg8bit/train"

    # source_dir_4 = "/home/m0rtzz/Workspaces/wmx_workspace/data/cityscapes/leftImg8bit/val"
    # target_dir_4 = "/home/m0rtzz/Workspaces/wmx_workspace/data/cityscapes_fisheye/leftImg8bit/val"

    # keyword = "labelTrainIds.png"

    # processImages(source_dir_1, target_dir_1, keyword)
    # processImages(source_dir_2, target_dir_2, keyword)
    # processImages(source_dir_3, target_dir_3, ".png")
    # processImages(source_dir_4, target_dir_4, ".png")

    source_dir_5 = "/home/m0rtzz/Workspaces/Fisheye_test/images/test/origin"
    target_dir_5 = "/home/m0rtzz/Workspaces/Fisheye_test/images/test/fisheye"
    processImages(source_dir_5, target_dir_5, ".png")

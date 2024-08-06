#!/home/m0rtzz/Programs/anaconda3/envs/VisionVoyage/bin/python3

"""
File: PT2fisheye.py
Author: M0rtzz
Create Date: 2023-10-20
Version: 1.0
Description: origin2fisheye.
"""


import math
import argparse
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


def getOneFisheye(img, pointx, pointy):
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


def processImages(image_paths, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for img_path in tqdm(image_paths):
        image_file = os.path.basename(img_path)
        target_path = os.path.join(target_dir, image_file)

        # if os.path.exists(target_path):
        #     continue

        img = cv2.imread(img_path)
        result = getOneFisheye(img, 0, 0)
        result = result[274:850, 704:1344]  # 裁剪成正方形
        cv2.imwrite(target_path, result)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some images.')
    parser.add_argument('image_paths', metavar='N', type=str, nargs='+',
                        help='an image path for processing')
    target_dir = "./images/my_images/fisheye_transformation/normal2fisheye"
    args = parser.parse_args()
    processImages(args.image_paths, target_dir)

#!/home/m0rtzz/Programs/anaconda3/envs/VisionVoyage/bin/python3

import argparse
import os
import cv2
from mmseg.apis import inference_model, init_model, show_result_pyplot

# NOTE: 禁止指定警告输出
import warnings
warnings.filterwarnings("ignore", message="torch.meshgrid*", category=UserWarning)

parser = argparse.ArgumentParser(description='Image Segmentation')
parser.add_argument('--image_paths', nargs='+', help='input image paths')
args = parser.parse_args()

normal_config_path = './scripts/configs/mask2former/mask2former_swin-t_8xb2-90k_normal.py'
normal_checkpoint_path = './scripts/weights/normal.pth'

fisheye_config_path = './scripts/configs/mask2former/CBAM4_swin-t_fisheye-mean.py'
fisheye_checkpoint_path = './scripts/weights/fisheye.pth'

config_path = ''
checkpoint_path = ''
output_dir = './assets/my_images/sem_seg/output/images'


def assignConfigByResolution(img_path):
    img = cv2.imread(img_path)
    height, width, _ = img.shape

    resolution_paths = {
        (2048, 1024): (normal_config_path, normal_checkpoint_path),
        (1280, 966): (fisheye_config_path, fisheye_checkpoint_path),
    }

    default_paths = (normal_config_path, normal_checkpoint_path)

    config_path, checkpoint_path = resolution_paths.get((width, height), default_paths)

    return config_path, checkpoint_path


if __name__ == '__main__':
    for img_path in args.image_paths:
        if img_path.endswith('.png') or img_path.endswith('.jpg'):
            config_path, checkpoint_path = assignConfigByResolution(img_path)
            filename = os.path.basename(img_path)
            output_path = os.path.join(output_dir, filename)

            # 构建模型
            model = init_model(config_path, checkpoint_path, device='cuda:0')

            # 推理
            result = inference_model(model, img_path)

            # 保存
            show_result_pyplot(model, img_path, result, show=False, save_dir=output_dir, out_file=output_path)

            cv2.namedWindow("Press ESC to exit", cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_NORMAL)
            cv2.resizeWindow("Press ESC to exit", 800, 600)  # 设置窗口大小为 800x600
            mat = cv2.imread(output_path)
            cv2.imshow("Press ESC to exit", mat)
            while True:
                if cv2.waitKey(1) == 27:  # 按下esc键的ASCII码为27
                    cv2.destroyWindow("Press ESC to exit")
                    break

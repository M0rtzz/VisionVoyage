# 开始：安装和运行 VisionVoyage

## ① 前提

此软件为 ZZU 计院的双创项目，主要实现基于鱼眼相机与感知技术的自动驾驶仿真系统。

环境为 Ubuntu20.04.6 LTS，需要 NVIDIA 的 GPU。

![image-20240430150629416](https://static.m0rtzz.com/images/Year:2024/Month:04/Day:30/15:06:29_image-20240430150629416.png)

拉取预训练权重：

```shell
sudo apt update -y && sudo apt install git-lfs -y
git-lfs pull
```

![image-20240627153649877](https://static.m0rtzz.com/images/Year:2024/Month:06/Day:27/15:36:49_image-20240627153649877.png)

---

## ② 安装

一些运行依赖：

```shell
sudo apt update
sudo apt install wmctrl sl pdftk libhpdf-dev libcrypto++-dev libeigen3-dev libgl1-mesa-glx libegl1-mesa-dev
sudo apt install libopencv-dev # 不支持CUDA和CUDNN
sudo ln -s /usr/include/opencv4/opencv2 /usr/include/
```

如果需要编译安装CUDA和CUDNN支持的OpenCV，可参考我的博客:

[博客](https://www.m0rtzz.com/posts/3#opencv420%E7%9A%84cmake%E5%91%BD%E4%BB%A4%E5%8F%8A%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9ubuntu2004%E8%A3%85%E8%BF%99%E4%B8%AA)

### （1）conda创建虚拟环境

```shell
conda create -n VisionVoyage python=3.8
```

```shell
conda activate VisionVoyage
```

```shell
conda install conda-forge::gcc=12.1.0
```

```shell
# 主要的包，其余的包如果报错，自行 `python3 -m pip install 包名` 安装
python3 -m pip install Pillow pyside6 python-alipay-sdk tqdm qrcode pygame 'pandas==1.2.0' 'seaborn==0.10.0' 'matplotlib==3.3.0' 'opencv-python==4.2.0.34' 'scipy==1.4.1' 'matplotlib>=3.2.2' 'PyYAML>=5.3.1' 'tqdm>=4.41.0' 'tensorboard>=2.4.1' 'pycocotools>=2.0'
```

然后安装CUDA版的Pytorch（1.7.0≤torch≤2.0.1，≥1.7.0是[multiyolov5库要求的](https://github.com/TomMao23/multiyolov5/blob/403db6287ab7f195931d076a2d64b1aaef9013b9/requirements.txt#L10)，最好装2.0.1，因为鄙人的版本是2.0.1，低版本和高版本鄙人没有测试过），根据官网命令安装：

[PyTorch 官网](https://pytorch.org/get-started/previous-versions/)

推荐使用南方科技大学提供的NVIDIA镜像channel（修改`~/.condarc`，同样推荐设置`env_dirs`，否则有可能虚拟环境默认在`~/.conda/envs/`中）：

```yaml
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  deepmodeling: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  nvidia: https://mirrors.sustech.edu.cn/anaconda-extra/cloud

envs_dirs:
  - /home/m0rtzz/Program_Files/anaconda3/envs
```

Pytorch安装完成后：

```shell
python3 -m pip install thop
```

之后安装 mmsegmentation：

```shell
python3 -m pip install -U openmim
mim install 'mmengine==0.10.3'
python3 -m pip install -U pip setuptools
mim install 'mmcv==2.1.0'

# 必须安装numpy==1.18.4
python3 -m pip uninstall numpy
python3 -m pip install 'numpy==1.18.4'
```

```shell
git clone -b v1.2.2 https://github.com/open-mmlab/mmsegmentation.git mmsegmentation-v1.2.2
```

添加`CBAMA4 neck`：

1）修改`mmsegmentation-v1.2.2/mmseg/models/necks/__init__.py`

```python
# Copyright (c) OpenMMLab. All rights reserved.
from .featurepyramid import Feature2Pyramid
from .fpn import FPN
from .ic_neck import ICNeck
from .jpu import JPU
from .mla_neck import MLANeck
from .multilevel_neck import MultiLevelNeck

# add CBAM4
from .CBAM import CBAM4

__all__ = [
    'FPN', 'MultiLevelNeck', 'MLANeck', 'ICNeck', 'JPU', 'Feature2Pyramid','CBAM4'
]
```

2）创建`mmsegmentation-v1.2.2/mmseg/models/necks/CBAM.py`

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from mmcv.cnn import ConvModule
from mmengine.model import BaseModule

from mmseg.registry import MODELS
from ..utils import resize

class ChannelAttention(nn.Module):
    def __init__(self, in_planes, ratio=16):
        super(ChannelAttention, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.max_pool = nn.AdaptiveMaxPool2d(1)

        self.fc1 = nn.Conv2d(in_planes, in_planes // ratio, 1, bias=False)
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Conv2d(in_planes // ratio, in_planes, 1, bias=False)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        avg_out = self.fc2(self.relu1(self.fc1(self.avg_pool(x))))
        max_out = self.fc2(self.relu1(self.fc1(self.max_pool(x))))
        out = avg_out + max_out
        return self.sigmoid(out)


class SpatialAttention(nn.Module):
    def __init__(self, kernel_size=7):
        super(SpatialAttention, self).__init__()

        assert kernel_size in (3, 7), 'kernel size must be 3 or 7'
        padding = 3 if kernel_size == 7 else 1

        self.conv1 = nn.Conv2d(2, 1, kernel_size, padding=padding, bias=False)  # 7,3     3,1
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        avg_out = torch.mean(x, dim=1, keepdim=True)
        max_out, _ = torch.max(x, dim=1, keepdim=True)
        x = torch.cat([avg_out, max_out], dim=1)
        x = self.conv1(x)
        return self.sigmoid(x)


class CBAM(nn.Module):
    def __init__(self, in_planes, ratio=16, kernel_size=7):
        super(CBAM, self).__init__()
        self.ca = ChannelAttention(in_planes, ratio)
        self.sa = SpatialAttention(kernel_size)

    def forward(self, x):
        out = x * self.ca(x)
        result = out * self.sa(out)
        return result


# 四层通道注意力机制
@MODELS.register_module()
class CBAM4(BaseModule):
    def __init__(self,
                 in_channels,
                 out_channels,
                 num_outs=4,
                 start_level=0,
                 end_level=-1,
                 conv_cfg=None,
                 norm_cfg=None

                 ):
        super().__init__()
        self.cbam0 = CBAM(in_channels[0])
        self.cbam1 = CBAM(in_channels[1])
        self.cbam2 = CBAM(in_channels[2])
        self.cbam3 = CBAM(in_channels[3])

    def forward(self, inputs):
        x0 = self.cbam0(inputs[0])
        x1 = self.cbam1(inputs[1])
        x2 = self.cbam2(inputs[2])
        x3 = self.cbam3(inputs[3])

        outs = []
        outs.append(x0)
        outs.append(x1)
        outs.append(x2)
        outs.append(x3)

        return tuple(outs)
```

3）创建`mmsegmentation-v1.2.2/configs/_base_/datasets/Woodscape.py`

修改`data_root`的路径（下载并解压到想要的位置，貌似不下载并设置也行）：

[https://datasetninja.com/woodscape#images](https://datasetninja.com/woodscape#images)

![image-20240430153625781](https://static.m0rtzz.com/images/Year:2024/Month:04/Day:30/15:36:25_image-20240430153625781.png)

```python
# dataset settings
dataset_type = 'WoodscapeDataset'
data_root = '/home/m0rtzz/Downloads/Compressed/dataset/woodscape-rgb-fisheye-DatasetNinja'
crop_size = (512, 512)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations'),

    dict(
        type='RandomResize',
        scale=(2048, 1024),
        ratio_range=(0.5, 2.0),
        keep_ratio=True),
    dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
    dict(type='RandomFlip', prob=0.5),
    dict(type='PhotoMetricDistortion'),
    dict(type='PackSegInputs')
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=(2048, 1024), keep_ratio=True),
    # add loading annotation after ``Resize`` because ground truth
    # does not need to do resize data transform
    dict(type='LoadAnnotations'),
    dict(type='PackSegInputs')
]
img_ratios = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
tta_pipeline = [
    dict(type='LoadImageFromFile', backend_args=None),
    dict(
        type='TestTimeAug',
        transforms=[
            [
                dict(type='Resize', scale_factor=r, keep_ratio=True)
                for r in img_ratios
            ],
            [
                dict(type='RandomFlip', prob=0., direction='horizontal'),
                dict(type='RandomFlip', prob=1., direction='horizontal')
            ], [dict(type='LoadAnnotations')], [dict(type='PackSegInputs')]
        ])
]
train_dataloader = dict(
    batch_size=8,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='InfiniteSampler', shuffle=True),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        data_prefix=dict(
            img_path='images/train', seg_map_path='gtLabels/train'),
        pipeline=train_pipeline))
val_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        data_prefix=dict(
            img_path='images/val', seg_map_path='gtLabels/val'),
        pipeline=test_pipeline))
test_dataloader = val_dataloader

val_evaluator = dict(type='IoUMetric', iou_metrics=['mIoU'])
test_evaluator = val_evaluator
```

之后将 mmsegmentaion 作为 editable mode 安装：

```shell
python3 -m pip install -v -e .
```

最后下载`VisionVOyage_Server`并安装CARLA的Python绑定库：[DOWNLOAD_VISIONVOYAGE_SERVER.md](./DOWNLOAD_VISIONVOYAGE_SERVER.md)

下载`VisionVoyage-Server-UE4.26-Shipping.tar.gz`，解压：

```shell
tar -xvf VisionVoyage-Server-UE4.26-Shipping.tar.gz
```

然后在`VisionVoyage_Server/PythonAPI/carla/dist/`中（记下`VisionVoyage_Server`文件夹的路径，下面要用到）：

```shell
cd VisionVoyage_Server/PythonAPI/carla/dist/ && conda activate VisionVoyage && python3 -m pip install ./carla-0.9.14-cp38-cp38-linux_x86_64.whl
```

### （2）申请支付宝当面付

因为软件集成了付费功能，所以需要开通支付宝的当面付功能

[https://b.alipay.com/page/product-workspace/product-detail/I1080300001000041016](https://b.alipay.com/page/product-workspace/product-detail/I1080300001000041016)

点击之后使用支付宝APP搜码或者使用账号密码登录，然后开通此产品：

![image-20240804152418499](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/15:24:23_image-20240804152418499.png)

经营类目选择`零售批发、杂货店`：

![image-20240804152715438](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/15:27:15_image-20240804152715438.png)

营业执照不填：

![image-20240804152806391](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/15:28:06_image-20240804152806391.png)

> [!WARNING]
>
> ![image-20240804153843474](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/15:38:43_image-20240804153843474.png)

店铺名字和图片可以去网上找一张旧照片，地址随意填一个：

![image-20240804153951004](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/15:39:51_image-20240804153951004.png)

填写姓名和手机接收到的验证码：

![image-20240804154137883](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/15:41:37_image-20240804154137883.png)

![image-20240804154235792](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/15:42:35_image-20240804154235792.png)

显示已开通后，点击开发设置：

![image-20240521142246943](https://static.m0rtzz.com/images%2FYear:2024%2FMonth:05%2FDay:21%2F14:22:47_image-20240521142246943.png)

创建应用并关联，创建后应该显示的是`开发中`，不是`上线`，获取到的AppID请妥善保存：

![image-20240804164036661](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/16:40:36_image-20240804164036661.png)

进入下面的网站开通：

[https://openhome.alipay.com/platform/appManage.htm#/apps](https://openhome.alipay.com/platform/appManage.htm#/apps)

![image-20240804164003553](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/16:40:03_image-20240804164003553.png)

此步骤的支付宝开放平台密钥工具官方只提供了Windows和Mac OS的版本：

![image-20240804155735037](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/15:57:35_image-20240804155735037.png)

![image-20240804160041005](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/16:00:41_image-20240804160041005.png)

![image-20240804160724762](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/16:07:31_image-20240804160724762.png)

获取到的应用私钥请妥善保存：

![image-20240804160947394](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/16:09:47_image-20240804160947394.png)

![image-20240804161036395](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/16:10:36_image-20240804161036395.png)

上传后获取到的支付宝公钥请妥善保存：

![image-20240804161218381](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/16:12:18_image-20240804161218381.png)

之后提交审核，审核完成后，应用状态将变为`上线`，此时将可以正常使用付费功能：

![image-20240804164108248](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/16:41:08_image-20240804164108248.png)

获取秘钥之后在`certs/`下创建`alipay_public_key.pem`和`app_private_key.pem`，分别对应支付宝公钥和应用私钥。

> [!IMPORTANT]
>
> ```txt
> 应用私钥格式：
> -----BEGIN RSA PRIVATE KEY-----
> 内容
> -----END RSA PRIVATE KEY-----
> 
> 支付宝公钥格式：
> -----BEGIN PUBLIC KEY-----
> 内容
> -----END PUBLIC KEY-----
> ```

修改`scripts/alipy.py`中的appid为自己的：

```python
class AlipayPayment:
    def __init__(self, app_private_key_path, alipay_public_key_path):
        self.app_private_key_string = open(app_private_key_path).read()
        self.alipay_public_key_string = open(alipay_public_key_path).read()
        self.alipay = AliPay(
            appid="your-appid",
            app_notify_url=None,
            app_private_key_string=self.app_private_key_string,
            alipay_public_key_string=self.alipay_public_key_string,
            sign_type="RSA2",
            debug=False
        )
```

### （3）修改路径

```shell
sudo chmod +x ./setup.sh && ./setup.sh
```

![image-20240804175012171](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/17:50:12_image-20240804175012171.png)

全部修改完成之后，编译C++源程序：

```shell
cd scripts/ && make
```

### （4）添加桌面图标

```shell
sudo chmod +x scripts/*.py scripts/*.sh scripts/*.out && ./scripts/init_desktop.sh
```

![image-20240430150536547](https://static.m0rtzz.com/images/Year:2024/Month:04/Day:30/15:05:36_image-20240430150536547.png)

## ③ 运行

```shell
./main.sh
```

或

双击桌面图标（右键设置为允许启动）

![image-20240430151406177](https://static.m0rtzz.com/images/Year:2024/Month:04/Day:30/15:14:11_image-20240430151406177.png)

## ④ Customize

设计GUI：

```shell
pyside6-designer main.ui
```

![image-20240804185843168](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/18:58:43_image-20240804185843168.png)

## ⑤ Runtime Error

### 1）分割图像

![image-20240806110627986](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:06/11:07:11_image-20240806110627986.png)

**解决办法：**

将`mmsegmentation-v1.2.2/mmseg/visualization/local_visualizer.py`中（Line 168-175）：

```python
mask = cv2.rectangle(mask, loc,
                     (loc[0] + label_width + baseline,
                      loc[1] + label_height + baseline),
                     classes_color, -1)
mask = cv2.rectangle(mask, loc,
                     (loc[0] + label_width + baseline,
                      loc[1] + label_height + baseline),
                     (0, 0, 0), rectangleThickness)
```

改为：

```python
mask = cv2.rectangle(mask, (loc[0], loc[1]),
                     (loc[0] + label_width + baseline,
                      loc[1] + label_height + baseline),
                     classes_color, -1)
mask = cv2.rectangle(mask, (loc[0], loc[1]),
                     (loc[0] + label_width + baseline,
                      loc[1] + label_height + baseline),
                     (0, 0, 0), rectangleThickness)
```

**Reference：**

[https://github.com/open-mmlab/mmsegmentation/issues/3409](https://github.com/open-mmlab/mmsegmentation/issues/3409)

### 2）分割视频

![image-20240806111334096](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:06/11:13:34_image-20240806111334096.png)

**解决办法：**

将`anaconda3/envs/mmsegmentation/lib/python3.8/site-packages/torch/nn/modules/upsampling.py`中（Line 155-157）：

```python
def forward(self, input: Tensor) -> Tensor:
    return F.interpolate(input, self.size, self.scale_factor, self.mode, self.align_corners, recompute_scale_factor=self.recompute_scale_factor)
```

改为：

```python
def forward(self, input: Tensor) -> Tensor:
    return F.interpolate(input, self.size, self.scale_factor, self.mode, self.align_corners)
```

> [!NOTE]
>
>   ***Updateing!!!***

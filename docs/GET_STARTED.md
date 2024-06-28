# 开始：安装和运行VisionVoyage

## ①前提

此软件为ZZU计院的双创项目，主要实现基于鱼眼相机与感知技术的自动驾驶仿真系统。

环境为Ubuntu20.04.6 LTS，需要NVIDIA的GPU。

![image-20240430150629416](https://cdn.jsdelivr.us/gh/M0rtzz/ImageHosting@master/images/Year:2024/Month:04/Day:30/15:06:29_image-20240430150629416.png)

拉取预训练权重：

```shell
sudo apt update -y && sudo apt install git-lfs -y
git-lfs pull
```

![image-20240627153649877](https://cdn.jsdelivr.us/gh/M0rtzz/ImageHosting/images/Year:2024/Month:06/Day:27/15:36:49_image-20240627153649877.png)

---

## ②安装

一些运行依赖：

```shell
sudo apt install wmctrl sl libhpdf-dev libcrypto++-dev libeigen3-dev
```

还需要编译安装OpenCV，可参考我的博客:

[https://blog.csdn.net/M0rtzz/article/details/136060074](https://blog.csdn.net/M0rtzz/article/details/136060074)

### （1）conda创建两个环境

#### 环境一

```shell
conda create -n py38 python=3.8
```

```shell
conda activate py38
```

```shell
conda install -c conda-forge gcc=12.1.0
```

```shell
# 主要的包，其余的包如果报错，自行 `python3 -m pip install 包名` 安装
python3 -m pip install pyside6 opencv-python==4.2.0.34 python-alipay-sdk tqdm matplotlib==3.3.0 qrcode pygame

# 必须安装numpy==1.18.4
python3 -m pip uninstall numpy
python3 -m pip install numpy==1.18.4
```

之后安装我提供的wheel包：[DOWNLOAD_VISIONVOYAGE_SERVER.md](./DOWNLOAD_VISIONVOYAGE_SERVER.md)

解压后在`PythonAPI/carla/dist/`中

![image-20240430142501765](https://cdn.jsdelivr.us/gh/M0rtzz/ImageHosting@master/images/Year:2024/Month:04/Day:30/14:25:06_image-20240430142501765.png)

```shell
conda activate py38 && python3 -m pip install ./carla-0.9.14-cp38-cp38-linux_x86_64.whl
```

---

#### 环境二

```shell
conda create -n mmsegmentation python=3.8
```

```shell
conda activate mmsegmentation
```

首选安装pytorch，需要GPU版，根据官网命令安装：

[PyTorch官网](https://pytorch.org/)

推荐使用校园联合镜像站中南方科技大学提供NVIDIA镜像channel（修改~/.condarc）：

```yaml
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  deepmodeling: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  nvidia: https://mirrors.cernet.edu.cn/anaconda-extra/cloud
```

之后安装mmsegmentation：

```shell
python3 -m pip install -U openmim
mim install mmengine==0.10.3
mim install mmcv==2.1.0
```

```shell
git clone -b v1.2.2 https://github.com/open-mmlab/mmsegmentation.git mmsegmentation-v1.2.2
```

添加`CBAMA4 neck`：

1）修改`mmseg/models/necks/__init__.py`

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

2）创建`mmseg/models/necks/CBAM.py`

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

3）创建`configs/_base_/datasets/Woodscape.py`

`data_root`的路径（下载并解压到想要的位置，貌似不下载并设置也行）：

[https://datasetninja.com/woodscape#images](https://datasetninja.com/woodscape#images)

![image-20240430153625781](https://cdn.jsdelivr.us/gh/M0rtzz/ImageHosting@master/images/Year:2024/Month:04/Day:30/15:36:25_image-20240430153625781.png)

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

之后将mmsegmentaion作为editable mode安装：

```shell
python3 -m pip install -v -e .
```

### （2）申请支付宝当面付

因为软件集成了付费功能，所以需要开通支付宝的当面付功能

[https://b.alipay.com/page/product-mall/all-product](https://b.alipay.com/page/product-mall/all-product)

![image-20240521142002149](/home/m0rtzz/.config/Typora/typora-user-images/image-20240521142002149.png)

点击之后使用支付宝APP搜码或者使用账号密码登录，然后开通此产品，显示已开通后，点击开发设置：

![image-20240521142246943](https://cdn.jsdelivr.us/gh/M0rtzz/ImageHosting@master/images/Year:2024/Month:05/Day:21/14:22:47_image-20240521142246943.png)

创建应用并关联：

![image-20240521142336673](https://cdn.jsdelivr.us/gh/M0rtzz/ImageHosting@master/images/Year:2024/Month:05/Day:21/14:23:36_image-20240521142336673.png)

之后获取秘钥：

![image-20240521143417101](https://cdn.jsdelivr.us/gh/M0rtzz/ImageHosting@master/images/Year:2024/Month:05/Day:21/14:34:17_image-20240521143417101.png)

具体步骤可参考此博客：

[https://blog.csdn.net/rankun1/article/details/92401295](https://blog.csdn.net/rankun1/article/details/92401295)

获取秘钥之后在`certs/`下创建`alipay_public_key.pem`和`app_private_key.pem`，分别对应支付宝公钥和应用私钥。

### （3）修改路径

1）`scripts/VisionVoyageServer.sh`

修改其中的`UE4_PROJECT_ROOT`为解压服务器压缩包后的文件夹路径[DOWNLOAD_VISIONVOYAGE_SERVER.md](./DOWNLOAD_VISIONVOYAGE_SERVER.md)

2）`scripts/`中的脚本和`main.py`

修改其中所有python脚本的首行解释器绝对路径为自己的，例如：

```python
#!/home/m0rtzz/Program_Files/anaconda3/envs/py38/bin/python3
```

全部修改完成之后，编译C++源程序：

```shell
cd scripts/ && make all
```

### （4）添加桌面图标

```shell
sudo chmod +x scripts/*.py scripts/*.sh scripts/*.out && ./init_desktop.sh
```

![image-20240430150536547](https://cdn.jsdelivr.us/gh/M0rtzz/ImageHosting@master/images/Year:2024/Month:04/Day:30/15:05:36_image-20240430150536547.png)

## ③运行

```shell
./main.sh
```

或

双击桌面图标（右键设置为允许启动）

![image-20240430151406177](https://cdn.jsdelivr.us/gh/M0rtzz/ImageHosting@master/images/Year:2024/Month:04/Day:30/15:14:11_image-20240430151406177.png)

>   [!NOTE]
>
>   ***<u>==Updateing!!!==</u>***


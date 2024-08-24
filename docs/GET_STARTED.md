# 开始：安装和运行 VisionVoyage

## ① 前提

此软件为ZZU计院的双创|生产实习项目，主要实现基于鱼眼相机与感知技术的自动驾驶仿真系统。

推荐环境为Ubuntu20.04.6 LTS，需要NVIDIA的GPU。

![image-20240812230954056](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:12/23:09:59_image-20240812230954056.png)

安装`git-lfs`：

```shell
sudo apt update -y && sudo apt install -y git-lfs && git-lfs install
```

克隆本项目：

```shell
GIT_LFS_SKIP_SMUDGE=1 git clone --recursive https://github.com/M0rtzz/VisionVoyage.git VisionVoyage && cd VisionVoyage/
```

拉取预训练权重：

```shell
git-lfs pull
```

![image-20240812192405100](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:12/19:24:10_image-20240812192405100.png)

---

## ② 安装

一些运行依赖：

```shell
sudo apt update -y
sudo apt install -y sl pv pigz pdftk wmctrl libhpdf-dev libeigen3-dev libcrypto++-dev
sudo apt install -y libopencv-dev && sudo ln -s /usr/include/opencv4/opencv2/ /usr/include/ # 不支持CUDA和CUDNN

# 以下安装clang/clang++为可选内容
sudo tee -a /etc/apt/sources.list.d/llvm-apt.list > /dev/null << EOF 
deb [arch=amd64] https://mirrors.tuna.tsinghua.edu.cn/llvm-apt/focal/ llvm-toolchain-focal main
# deb-src [arch=amd64] https://mirrors.tuna.tsinghua.edu.cn/llvm-apt/focal/ llvm-toolchain-focal main
EOF

# 备份
sudo cp /etc/apt/sources.list.d/llvm-apt.list /etc/apt/sources.list.d/llvm-apt.list.save

# 只安装了clang/clang++，其他LLVM工具集自行选择安装
sudo apt update -y && sudo apt upgrade -y && sudo apt install -y clang
```

如果需要编译安装CUDA和CUDNN支持的OpenCV，可参考鄙人的博客:

[博客](https://www.m0rtzz.com/posts/3#opencv420%E7%9A%84cmake%E5%91%BD%E4%BB%A4%E5%8F%8A%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9ubuntu2004%E8%A3%85%E8%BF%99%E4%B8%AA)

### （1）conda创建虚拟环境

>   [!CAUTION]
>
>   因CARLA的Python绑定库whl文件是鄙人用CPython3.8环境编译出来的，所以创建的虚拟环境必须是Python3.8：
>
>   ```shell
>   conda create -n VisionVoyage python=3.8
>   ```

```shell
conda activate VisionVoyage
```

```shell
conda install conda-forge::gcc=12.1.0 conda-forge::gxx=12.1.0
```

```shell
# 主要的包，其余的包如果报错，自行 `python3 -m pip install 包名` 安装
python3 -m pip install lit cmake ftfy regex qrcode pygame fsspec Pillow pyside6 jmespath filelock packaging python-alipay-sdk 'lxml==4.4.1' 'onnx==1.13.0' 'scipy==1.4.1' 'pandas==1.2.0' 'seaborn==0.10.0' 'tomlkit==0.10.1' 'Twisted==22.10.0' 'matplotlib==3.2.0' 'service-identity==18.1.0' 'tqdm>=4.41.0' 'PyYAML>=5.3.1' 'pycocotools>=2.0' 'tensorboard>=2.4.1'
```

然后安装CUDA版的Pytorch（`1.7.0≤torch≤2.1.2`，≥1.7.0是[multiyolov5库要求的](https://github.com/TomMao23/multiyolov5/blob/403db6287ab7f195931d076a2d64b1aaef9013b9/requirements.txt#L10)，最好装`2.0.0≤torch≤2.1.2`，更低版本鄙人没有测试过，但是更高版本经测试安装`mmcv`时会有一些奇奇怪怪的编译错误，所以才有`1.7.0≤torch≤2.1.2`这个结论【bushi），根据官网命令安装：

[PyTorch官网](https://pytorch.org/get-started/previous-versions/)

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
  - /home/m0rtzz/Programs/anaconda3/envs
```

Pytorch安装完成后：

```shell
python3 -m pip install thop
```

之后安装mmsegmentation：

```shell
python3 -m pip install -U openmim
python3 -m pip install -U pip setuptools
mim install 'mmengine==0.10.3'
mim install 'mmcv==2.1.0'
mim install 'mmdet==3.2.0'

# 必须安装opencv-python==4.5.2.52（其实≥4.5.2.52也行，＜4.5.2.52将会产生一些Runtime Error）和numpy==1.18.4（VisionVoyageServer需要此版本）
yes | python3 -m pip uninstall opencv-python numpy
python3 -m pip install 'opencv-python==4.5.2.52' 'numpy==1.18.4'
```

之后将mmsegmentaion作为editable mode安装：

```shell
git submodule update --recursive # 如果 `3rdparty/mmsegmentation-v1.2.2/` 为空，执行此命令
cd 3rdparty/mmsegmentation-v1.2.2/ && python3 -m pip install --use-pep517 -v -e .
```

最后下载`VisionVoyage_Server`并安装CARLA的Python绑定库：[DOWNLOAD_VISIONVOYAGE_SERVER.md](./DOWNLOAD_VISIONVOYAGE_SERVER.md)

下载`VisionVoyageServer-UE4.26-Shipping.tar.gz`到`server/`，解压：

```shell
cd server/ && pv VisionVoyageServer-UE4.26-Shipping.tar.gz | pigz -d | tar xf -  # 解压之后是一个名为 `VisionVoyageServer` 的文件夹
```

然后安装CARLA的Python绑定库：

```shell
cd server/VisionVoyage_Server/PythonAPI/carla/dist/ && conda activate VisionVoyage && python3 -m pip install ./carla-0.9.14-cp38-cp38-linux_x86_64.whl
```

### （2）申请支付宝当面付

因为软件集成了付费功能，所以需要开通支付宝的当面付功能

[https://b.alipay.com/page/product-workspace/product-detail/I1080300001000041016](https://b.alipay.com/page/product-workspace/product-detail/I1080300001000041016)

点击之后使用支付宝APP搜码或者使用账号密码登录，然后开通此产品：

![image-20240804152418499](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/15:24:23_image-20240804152418499.png)

经营类目选择`零售批发、杂货店`：

![image-20240804152715438](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/15:27:15_image-20240804152715438.png)

营业执照不上传：

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
> `alipay_public_key.pem`格式：
>
> ```txt
> -----BEGIN PUBLIC KEY-----
> 内容
> -----END PUBLIC KEY-----
> ```
>
> `app_private_key.pem`格式：
>
> ```txt
> -----BEGIN RSA PRIVATE KEY-----
> 内容
> -----END RSA PRIVATE KEY-----
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

### （3）下载数据集（Optional）

> [!NOTE]
>
> 如果需要数据集测试、训练的，可以参考以下文档下载。

[DOWNLOAD_DATASETS.md](./DOWNLOAD_DATASETS.md)

### （4）修改路径

```shell
conda activate VisionVoyage && sudo chmod +x ./setup.sh && ./setup.sh
```

![image-20240811174253243](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:11/17:42:58_image-20240811174253243.png)

全部修改完成之后，编译C++源程序：

```shell
cd scripts/ && make
```

### （5）添加桌面图标

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

**设计GUI：**

```shell
conda activate VisionVoyage && QT_LOGGING_RULES='*.debug=false;qt.pysideplugin=false' pyside6-designer main.ui
```

![image-20240804185843168](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:04/18:58:43_image-20240804185843168.png)

修改之后首先`Ctrl + S`保存`main.ui`文件，之后点击：

![image-20240806173718025](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:06/17:37:18_image-20240806173718025.png)

将Python代码复制下来（绿色框）或者保存（红色框）覆盖`modules/ui_main.py`：

![image-20240806173852946](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:06/17:38:53_image-20240806173852946.png)

或（保存`main.ui`文件之后）：

```shell
# Convert UI
conda activate VisionVoyage && pyside6-uic main.ui > modules/ui_main.py
```

---

**添加或修改图片资源（需要在`resources.qrc`中添加）：**

```xml
<qresource prefix="images">
  <file>assets/images/VisionVoyage.png</file>
  <file>assets/images/VisionVoyage_vertical.png</file>
  <file>assets/images/IngenuityDrive.png</file>
  <file>assets/images/sensors.png</file>
  <file>assets/images/fisheye_rgb.png</file>
  <file>assets/images/fisheye_semantic.png</file>
  <file>assets/images/fisheye_collage.png</file>
</qresource>
```

之后执行以下命令整合：

```shell
# Convert QRC
conda activate VisionVoyage && pyside6-rcc resources.qrc -o resources_rc.py && cp resources_rc.py modules/resources_rc.py
```

这样就完成了GUI的设计。

## ⑤ Runtime Error

### 支付接口

![image-20240806144820760](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:06/14:48:20_image-20240806144820760.png)

**解决办法：**

电脑端登入[商家平台](http://b.alipay.com/)，点击右上角【铃铛】后，在【系统通知】中查看对应通知内容，并点击进入操作补全。

![image-20240806150115646](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:06/15:01:15_image-20240806150115646.png)

**Reference：**

[https://opendocs.alipay.com/support/07cfbk](https://opendocs.alipay.com/support/07cfbk)

> [!NOTE]
>
> ***Updateing!!!***

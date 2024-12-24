# 开始：安装和运行VisionVoyage

## ① 前提

此软件为`ZZU`计院的双创|生产实习项目，主要实现基于鱼眼相机与感知技术的自动驾驶仿真系统。

推荐环境为`Ubuntu20.04.6 LTS`，需要`NVIDIA`的`GPU`。

![fastfetch](./.figures/GET_STARTED/fastfetch.png)

安装`git-lfs`：

```shell
sudo apt update -y && sudo apt install -y git-lfs
```

克隆本项目并配置`git-lfs`：

```shell
GIT_LFS_SKIP_SMUDGE=1 git clone --recursive https://github.com/M0rtzz/VisionVoyage.git VisionVoyage && cd VisionVoyage/ && git-lfs install
```

拉取视频和预训练权重：

```shell
git-lfs pull
```

![git-lfs_pull](./.figures/GET_STARTED/git-lfs_pull.png)

---

## ② 安装

一些运行依赖：

```shell
sudo apt update -y
sudo apt install -y sl pv pigz pdftk wmctrl libhpdf-dev libeigen3-dev libcrypto++-dev
sudo apt install -y libopencv-dev && sudo ln -s /usr/include/opencv4/opencv2/ /usr/include/ # 不支持CUDA和cuDNN

# 以下安装clang/clang++为可选内容
wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | sudo apt-key add - && \
sudo tee /etc/apt/sources.list.d/llvm.list > /dev/null << EOF
deb [arch=amd64] https://mirrors.hust.edu.cn/llvm-apt/focal/ llvm-toolchain-focal main
# deb-src [arch=amd64] https://mirrors.hust.cn/llvm-apt/focal/ llvm-toolchain-focal main
EOF

# 备份
sudo cp /etc/apt/sources.list.d/llvm.list /etc/apt/sources.list.d/llvm-apt.list.save

# 只安装了clang/clang++，其他LLVM工具集自行选择安装
sudo apt update -y && sudo apt upgrade -y && sudo apt install -y clang
```

如果需要编译安装`CUDA`和`cuDNN`支持的`OpenCV`，可参考鄙人的博客:

[博客](https://www.m0rtzz.com/posts/3#cmake命令)

### （1）conda创建虚拟环境

> [!CAUTION]
>
> 因`CARLA`的`Python`绑定库`whl`文件是鄙人用`CPython3.8`环境编译出来的，所以创建的虚拟环境必须是`Python3.8`：
>
> ```shell
> conda create -n VisionVoyage python=3.8
> ```

```shell
conda activate VisionVoyage
```

```shell
conda install conda-forge::gcc=12.1.0 conda-forge::gxx=12.1.0
```

```shell
# 主要的包，其余的包如果报错缺失，自行 `python3 -m pip install 包名` 安装
python3 -m pip install lit cmake ftfy regex qrcode pygame fsspec Pillow pyside6 jmespath filelock packaging python-alipay-sdk 'lxml==4.4.1' 'onnx==1.13.0' 'scipy==1.4.1' 'pandas==1.2.0' 'seaborn==0.10.0' 'tomlkit==0.10.1' 'Twisted==22.10.0' 'matplotlib==3.2.0' 'service-identity==18.1.0' 'tqdm>=4.41.0' 'PyYAML>=5.3.1' 'pycocotools>=2.0' 'tensorboard>=2.4.1'
```

然后安装`CUDA`版的`Pytorch`（`1.7.0≤torch≤2.1.2`，≥1.7.0是[multiyolov5库要求的](https://github.com/TomMao23/multiyolov5/blob/master/requirements.txt#L10)，最好装`2.0.0≤torch≤2.1.2`，更低版本鄙人没有测试过，但是更高版本经测试安装`mmcv`时会有一些奇奇怪怪的编译错误，所以才有`1.7.0≤torch≤2.1.2`这个结论【bushi），根据官网命令安装：

[PyTorch官网](https://pytorch.org/get-started/previous-versions/)

推荐使用南方科技大学提供的`NVIDIA`镜像`channel`（修改`~/.condarc`，同样推荐设置`env_dirs`，否则有可能虚拟环境默认在`~/.conda/envs/`中）：

```yaml
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2/
custom_channels:
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
  numba: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
  pyviz: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
  omnia: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
  ohmeta: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
  plotly: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
  fastai: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
  caffe2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
  Paddle: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
  dglteam: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
  rapidsai: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
  MindSpore: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
  pytorch3d: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
  pytorch-test: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
  nvidia: https://mirrors.sustech.edu.cn/anaconda-extra/cloud/

envs_dirs:
  - /home/m0rtzz/Programs/anaconda3/envs
```

`Pytorch`安装完成后：

```shell
python3 -m pip install thop
```

之后安装`mmsegmentation`：

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

之后将`mmsegmentaion`作为`editable mode`安装：

```shell
git submodule update --recursive # 如果 `3rdparty/mmsegmentation-v1.2.2/` 为空，执行此命令
cd 3rdparty/mmsegmentation-v1.2.2/ && python3 -m pip install --use-pep517 -v -e .
```

最后下载`VisionVoyageServer`并安装`CARLA`的`Python`绑定库：[DOWNLOAD_VISIONVOYAGE_SERVER.md](./DOWNLOAD_VISIONVOYAGE_SERVER.md)

下载`VisionVoyageServer-UE4.26-Shipping.tar.gz`到`server/`，解压：

```shell
cd server/ && pv VisionVoyageServer-UE4.26-Shipping.tar.gz | pigz -d | tar xf -  # 解压之后是一个名为 `VisionVoyageServer` 的文件夹
```

然后安装`CARLA`的`Python`绑定库：

```shell
cd server/VisionVoyageServer/PythonAPI/carla/dist/ && conda activate VisionVoyage && python3 -m pip install ./carla-0.9.14-cp38-cp38-linux_x86_64.whl
```

### （2）申请支付宝当面付

因为软件集成了付费功能，所以需要开通支付宝的当面付功能：

[https://b.alipay.com/page/product-workspace/product-detail/I1080300001000041016](https://b.alipay.com/page/product-workspace/product-detail/I1080300001000041016)

点击之后使用支付宝`APP`扫码或者使用账号密码登录，然后开通此产品：

![alipay_1](./.figures/GET_STARTED/alipay_1.png)

经营类目选择`零售批发、杂货店`：

![alipay_2](./.figures/GET_STARTED/alipay_2.png)

营业执照不上传：

![alipay_3](./.figures/GET_STARTED/alipay_3.png)

> [!WARNING]
>
> ![alipay_4](./.figures/GET_STARTED/alipay_4.png)

店铺名字和图片可以去网上找一张旧照片，地址随意填一个：

![alipay_5](./.figures/GET_STARTED/alipay_5.png)

填写姓名和手机接收到的验证码：

![alipay_6](./.figures/GET_STARTED/alipay_6.png)

![alipay_7](./.figures/GET_STARTED/alipay_7.png)

显示已开通后，点击开发设置：

![alipay_8](./.figures/GET_STARTED/alipay_8.png)

创建应用并关联，创建后应该显示的是`开发中`，不是`上线`，获取到的`AppID`请妥善保存：

![alipay_9](./.figures/GET_STARTED/alipay_9.png)

进入下面的网站开通：

[https://openhome.alipay.com/platform/appManage.htm#/apps](https://openhome.alipay.com/platform/appManage.htm#/apps)

![alipay_10](./.figures/GET_STARTED/alipay_10.png)

此步骤的支付宝开放平台密钥工具官方只提供了`Windows`和`Mac OS`的版本：

![alipay_11](./.figures/GET_STARTED/alipay_11.png)

![alipay_12](./.figures/GET_STARTED/alipay_12.png)

![alipay_13](./.figures/GET_STARTED/alipay_13.png)

获取到的应用私钥请妥善保存：

![alipay_14](./.figures/GET_STARTED/alipay_14.png)

![alipay_15](./.figures/GET_STARTED/alipay_15.png)

上传后获取到的支付宝公钥请妥善保存：

![alipay_16](./.figures/GET_STARTED/alipay_16.png)

之后提交审核，审核完成后，应用状态将变为`上线`，此时将可以正常使用付费功能：

![alipay_17](./.figures/GET_STARTED/alipay_17.png)

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

修改`scripts/alipy.py`中的`appid`为自己的：

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
> 如果需要数据集测试、训练，可以参考以下文档下载。

[DOWNLOAD_DATASETS.md](./DOWNLOAD_DATASETS.md)

### （4）修改路径

```shell
conda activate VisionVoyage && sudo chmod +x ./setup.sh && ./setup.sh
```

![setup](./.figures/GET_STARTED/setup.png)

全部修改完成之后，编译`C++`源程序：

```shell
cd scripts/ && make
```

### （5）添加桌面图标

```shell
sudo chmod +x scripts/*.py scripts/*.sh scripts/*.out && ./scripts/init_desktop.sh
```

![desktop](./.figures/GET_STARTED/desktop.png)

## ③ 运行

```shell
./main.sh
```

或

双击桌面图标（右键设置为允许启动）

![GUI](./.figures/GET_STARTED/GUI.png)

## ④ Customize

**设计GUI：**

```shell
conda activate VisionVoyage && QT_LOGGING_RULES='*.debug=false;qt.pysideplugin=false' pyside6-designer main.ui
```

![customize_1](./.figures/GET_STARTED/customize_1.png)

修改之后首先`Ctrl + S`保存`main.ui`文件，之后点击：

![customize_2](./.figures/GET_STARTED/customize_2.png)

将`Python`代码复制下来（绿色框）或者保存（红色框）覆盖`modules/ui_main.py`：

![customize_3](./.figures/GET_STARTED/customize_3.png)

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

这样就完成了`GUI`的设计。

## ⑤ Runtime Error

### 支付接口

![error_1](./.figures/GET_STARTED/error_1.png)

**解决办法：**

电脑端登入[商家平台](http://b.alipay.com/)，点击右上角【铃铛】后，在【系统通知】中查看对应通知内容，并点击进入操作补全。

![error_2](./.figures/GET_STARTED/error_2.png)

> **Reference：**
>
> [https://opendocs.alipay.com/support/07cfbk](https://opendocs.alipay.com/support/07cfbk)

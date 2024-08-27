# DOWNLOAD DATASETS

## 1.HuggingFace Datasets (Inside and outside the GFW)

[HuggingFace_URL](https://huggingface.co/datasets/M0rtzz/VisionVoyage/tree/main)

![HuggingFace](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:12/14:08:33_image-20240812140828114.png)

可以使用[国内镜像站](https://hf-mirror.com/)：

```shell
sudo apt update -y && sudo apt install -y curl aria2
```

下载`hfd.sh`到系统目录，这样全局都可以直接使用`hfd`命令：

```shell
sudo wget -q --show-progress https://hf-mirror.com/hfd/hfd.sh -O /usr/bin/hfd
sudo chmod a+x /usr/bin/hfd
```

**设置环境变量：**

```shell
echo 'export HF_ENDPOINT=https://hf-mirror.com' >> ~/.bashrc && source ~/.bashrc # 当前用户和Bash适用

echo 'export HF_ENDPOINT=https://hf-mirror.com' >> ~/.zshrc && source ~/.zshrc # 当前用户和z-shell适用

# 或者

echo 'export HF_ENDPOINT=https://hf-mirror.com' | sudo tee -a /etc/profile && source /etc/profile # 所有用户和Shell解释器都适用

# 需要取消镜像设置时，只需 `unset HF_ENDPOINT` 即可

# 不想全局设置的话，每次使用 `hfd` 前，手动在当前终端 `export HF_ENDPOINT=https://hf-mirror.com`
```

`hfd.sh`文档：

[README](./Huggingface_Model_Downloader.md)

下载数据集命令：

```shell
repo_root_dir=$(git rev-parse --show-toplevel) && \
export HF_ENDPOINT=https://hf-mirror.com && \
hfd \
M0rtzz/VisionVoyage \
--dataset True \
--local-dir ${repo_root_dir}/.temp/ \
--tool aria2c -x 8 && \
mv ${repo_root_dir}/.temp/*.tar ${repo_root_dir}/datasets/ && \
rm -rf ${repo_root_dir}/.temp/

# 从上到下参数依次为：
# repo_id：仓库id
# 下载类型是数据集
# 本地路径
# 设置下载工具为aria2c的线程数，默认是4
```

![image-20240812153102687](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:12/15:31:02_image-20240812153102687.png)

因为`Cityscapes_part_1.tar`和`Cityscapes_part_2.tar`是用`split`命令拆分的，所以下载完成后需要合并一下：

```shell
cd datasets/ && ls -a ./
pv Cityscapes_part_*.tar > Cityscapes.tar && rm Cityscapes_part_*.tar
```

![image-20240812154708590](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:12/15:47:08_image-20240812154708590.png)

之后解压：

```shell
pv Cityscapes.tar | pigz -d | tar xf - && pv WoodScape.tar | pigz -d | tar xf - && rm -f *.tar
```

![image-20240812155708816](https://static.m0rtzz.com/images/Year:2024/Month:08/Day:12/15:57:08_image-20240812155708816.png)

## 2.BaiDuNetDisk (Inside the GFW)

[Cityscapes](https://pan.baidu.com/s/1W-CN19oJuumFL3zr9hrq2g?pwd=1226)

[WoodScape](https://pan.baidu.com/s/1GFmx-Mfb8NVkFyuvkV8eLA?pwd=1226)

下载到`datasets/`下解压：

```shell
cd datasets/ && pv Cityscapes.tar | pigz -d | tar xf - && pv WoodScape.tar | pigz -d | tar xf - && rm -f *.tar
```

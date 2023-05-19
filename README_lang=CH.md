# 如果你不会使用Conda或者没有使用conda
请确保你使用的是python3.6版本,更高或者更低的版本都有可能导致出错
1. 使用如下指令安装python-ppt所需要的依赖
    ```bash
    pip install lxml
    pip install pillow
    pip install xlsxwriter
    ```
2. 安装python-ppt
    ```bash
    pip install python-pptx
    ```
# 创建 Conda 环境并安装 python-pptx

要在 Conda 环境中安装和使用 python-pptx，请按照以下步骤进行操作：

1. 打开终端或命令提示符。

2. 运行以下命令创建一个新的 Conda 环境：

   ```bash
   conda create -n py4ppt python=3.6
   ```

   这将创建一个名为 "py4ppt" 的新环境，Python 版本为 3.6。你可以将环境名称 ("py4ppt") 更改为你喜欢的名称。

3. 运行以下命令激活新创建的环境：

   ```bash
   conda activate py4ppt
   ```

4. 运行以下命令安装所需的依赖项：

   ```bash
   conda install -c conda-forge lxml
   conda install -c conda-forge pillow
   conda install -c conda-forge xlsxwriter
   ```

   这些命令将使用 Conda 包管理器安装所需的依赖项（lxml、Pillow 和 XlsxWriter）。

5. 最后，运行以下命令安装 python-pptx：

   ```bash
   pip install python-pptx
   ```

   这将使用 pip 从 PyPI 安装 python-pptx 包。

6. 现在你已成功在 Conda 环境中安装了 python-pptx。你可以通过导入 `pptx` 模块在 Python 脚本中开始使用它。

在每次使用 python-pptx 进行项目开发时，请记得激活你的 Conda 环境（`conda activate py4ppt`）。

注意：在按照这些说明之前，请确保你已经正确安装和设置了 Conda 和 pip。

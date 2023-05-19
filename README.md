[中文版本README](./README_lang=CH.md)
# Instructions

1. Place the PowerPoint files you want to extract text from in the `input` directory.

2. Run `demo.py` using the following command:

   ```bash
   python demo.py
   ```

   This script will process the PPT files in the `input` directory and extract the text content. The extracted text will be saved in separate text files in the `output` directory.

3. If you want to merge all the output content into a single file, you can run `sum.py` using the following command:

   ```bash
   python sum.py
   ```

   This script will combine all the text files in the `output` directory into a file named `sum.txt`. The `sum.txt` file will be located in the `output` directory.

   Note: Make sure you have the necessary permissions to read and write files in the respective directories.

# requirement
- python3.6
- lxml
- pillow
- xlsxwriter
- python-pptx
## Creating Conda Environment and Installing python-pptx

To install and use python-pptx in a Conda environment, follow these steps:

1. Open your terminal or command prompt.

2. Create a new Conda environment by running the following command:

   ```bash
   conda create -n py4ppt python=3.6
   ```

   This will create a new environment named "py4ppt" with Python version 3.6. You can change the environment name ("py4ppt") to your preferred name.

3. Activate the newly created environment by running the following command:

   ```bash
   conda activate py4ppt
   ```

4. Install the required dependencies by running the following commands:

   ```bash
   conda install -c conda-forge lxml
   conda install -c conda-forge pillow
   conda install -c conda-forge xlsxwriter
   ```

   These commands will install the necessary dependencies (lxml, Pillow, and XlsxWriter) using the Conda package manager.

5. Finally, install python-pptx by running the following command:

   ```bash
   pip install python-pptx
   ```

   This will install the python-pptx package from PyPI using pip.

6. You have now successfully installed python-pptx in your Conda environment. You can start using it in your Python scripts by importing the `pptx` module.

Remember to activate your Conda environment (`conda activate py4ppt`) every time you want to use python-pptx in your projects.

Note: Make sure you have Conda and pip installed and properly set up before following these instructions.

import ppt2Doc
import os

input_directory = 'input/'
output_directory = 'output/'

# Iterate through all files in the input directory
for filename in os.listdir(input_directory):
    # Get the full path of the file
    file_path = os.path.join(input_directory, filename)
    
    # Check if the file is a pptx file
    if filename.endswith('.pptx'):
        # Call the ppt_to_txt function to process the pptx file
        ppt2Doc.ppt_to_txt(file_path, output_directory)

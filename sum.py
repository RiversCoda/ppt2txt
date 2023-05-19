import os
output_directory = 'output/'
txt_files = [os.path.join(output_directory, file) for file in os.listdir(output_directory) if file.endswith('.txt')]
txt_files.sort()
with open(os.path.join(output_directory, 'sum.txt'), 'w', encoding='utf-8') as output_file:
    for txt_file in txt_files:
        with open(txt_file, 'r', encoding='utf-8') as input_file:
            output_file.write(f'Content from file: {os.path.basename(txt_file)}\n')
            output_file.write(input_file.read())
            output_file.write('\n')
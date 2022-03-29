import os
# 98121-5009 celene
def list_files(startpath):

    with open("folder_structure.txt", "w") as f_output:
        exclude_folders = ['.idea','__pycache__','.venv','']
        for root, dirs, files in os.walk(startpath):            
            level = root.replace(startpath, '').count(os.sep)
            indent = '\t' * 1 * (level)
            output_string = '{}{}/'.format(indent, os.path.basename(root))
           
            if(str(os.path.basename(root)) not in exclude_folders):
            
                print(output_string)
                f_output.write(output_string + '\n')
                subindent = '\t' * 1 * (level + 1)
                for f in files:
                    output_string = '{}{}'.format(subindent, f)
                    print(output_string)
                    f_output.write(output_string + '\n')

list_files(".")
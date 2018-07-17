import os, sys
from fileinput import FileInput

text_to_replace = 'DotnetTddStarter'
project_name = sys.argv[1]

lstDir = os.walk('.') 
for root, dirs, files in lstDir:
    for file in files:
        if (file != 'rename_project.py'):
            path = os.path.join(root, file)
            if '.git' not in path:
                for line in FileInput(os.path.join(root, file), inplace=True):
                    print(line.replace(text_to_replace, project_name), end='')

        if text_to_replace in file:
            new_file_name = file.replace(text_to_replace, project_name)
            os.rename(os.path.join(root, file), os.path.join(root, new_file_name))
    for dir in dirs:
        if '.git' not in dir:
            walk = os.walk(os.path.join(root, dir))
            for dir_root, sub_dirs, sub_files in walk:
                for sub_file in sub_files:
                    if (sub_file != 'rename_project.py'):
                        path = os.path.join(dir_root, sub_file)
                        if '.git' not in path:
                            macs = {project_name: text_to_replace}
                            for line in FileInput(os.path.join(dir_root, sub_file), inplace=True):
                                print(line.replace(text_to_replace, project_name), end='')

                    new_file_name = sub_file.replace(text_to_replace, project_name)
                    os.rename(os.path.join(dir_root, sub_file), os.path.join(dir_root, new_file_name))

        if text_to_replace in dir:
            new_dir_name = dir.replace(text_to_replace, project_name)
            os.rename(os.path.join(root, dir), os.path.join(root, new_dir_name))
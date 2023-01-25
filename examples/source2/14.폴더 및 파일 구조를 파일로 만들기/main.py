import seedir as sd
import os

찾을폴더_경로 = "../../"

for (path, dir, files) in os.walk(찾을폴더_경로):
    print(path)
    for filename in files:
        print(filename)

print("===================================================")

sd.seedir(찾을폴더_경로, style='emoji')

print("===================================================")

dir_tree  = sd.seedir(찾을폴더_경로, printout=False, style='emoji')

print(dir_tree)

print("===================================================")

save_file_path = "tree.txt"
with open(save_file_path, 'w', encoding='UTF8') as f : 
    f.write(dir_tree)
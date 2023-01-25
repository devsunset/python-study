import os
import shutil

path = "폴더1"
move_path = "폴더2"

for dirpath, dirname, files in os.walk(path):
    print(dirpath)
    for filename in files:

        try:
            print(os.path.join(dirpath, filename))
            shutil.move(os.path.join(dirpath, filename), move_path)
        except:
            pass
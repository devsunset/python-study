import seedir as sd

찾을폴더_경로 = r"C:\일잘러 파이썬과 40개의 작품들 코드"

dir_tree  = sd.seedir(찾을폴더_경로, printout=False, style='emoji')

save_file_path = r"14.폴더 및 파일 구조를 파일로 만들기\tree.txt"
with open(save_file_path, 'w', encoding='UTF8') as f : 
    f.write(dir_tree)
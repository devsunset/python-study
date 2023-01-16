import seedir as sd

찾을폴더_경로 = r"C:\일잘러 파이썬과 40개의 작품들 코드"

dir_tree = sd.seedir(찾을폴더_경로, printout=False, include_files='.*\.py',
                    regex=True, style='emoji')

print(dir_tree)
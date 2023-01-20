import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

excel_file_path = '이름_점수_이메일.xlsx'

df_from_excel = pd.read_excel(excel_file_path)

name_list = df_from_excel['이름'].tolist()
score_list = df_from_excel['점수'].tolist()
email_list = df_from_excel['이메일'].tolist()

print("이름:",name_list)
print("점수:",score_list)
print("이메일:",email_list)
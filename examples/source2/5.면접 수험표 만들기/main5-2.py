import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

df_from_excel = pd.read_excel("수험번호.xlsx")

이름_list = df_from_excel['이름'].to_list()
수험번호_list = df_from_excel['수험번호'].to_list()

print("이름:",이름_list)
print("수험번호:",수험번호_list)
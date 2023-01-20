import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

df_from_excel = pd.read_excel("수험번호.xlsx")

이름 = iter(df_from_excel['이름'])
수험번호 = iter(df_from_excel['수험번호'])

for i in range(10):
    print(next(이름),next(수험번호))
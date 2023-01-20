# pip install folium
# pip install openpyxl
# https://kess.kedi.re.kr/inedx
# https://www.vworld.kr/dev/v4dv_geocoderguide2_s001.do
import pandas as pd

# 판다스에서 학교명과 주소 찾는 처리

filePath = '고등교육기관 하반기 주소록(2020).xlsx'
df_from_excel = pd.read_excel(filePath,engine='openpyxl')

df_from_excel.columns = df_from_excel.loc[4].tolist()

df_from_excel = df_from_excel.drop(index=list(range(0,5)))

print(df_from_excel.head())

print(df_from_excel['학교명'].values)

print(df_from_excel['주소'].values)
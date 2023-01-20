# pip install folium
# pip install openpyxl
# https://kess.kedi.re.kr/inedx
# https://www.vworld.kr/dev/v4dv_geocoderguide2_s001.do
import pandas as pd
import folium

# 자료의 모든 대학교 주소에 마커 표시 처리

filePath = '학교주소좌표.xlsx'
df_from_excel = pd.read_excel(filePath,engine='openpyxl',header=None)

df_from_excel.columns = ['학교이름','주소','x','y']

name_list = df_from_excel['학교이름'].to_list()
addr_list = df_from_excel['주소'].to_list()
position_x_list = df_from_excel['x'].to_list()
position_y_list = df_from_excel['y'].to_list()

map = folium.Map(location=[37,127],zoom_start=7)

for i in range(len(name_list)):
    if position_x_list[i] != 0:
        marker = folium.Marker([position_y_list[i],position_x_list[i]],
                            popup=name_list[i], 
                            icon = folium.Icon(color='blue'))
        marker.add_to(map) 

map.save('uni_map.html')
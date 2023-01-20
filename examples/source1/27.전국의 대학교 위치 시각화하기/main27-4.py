# pip install folium
# pip install openpyxl
# https://kess.kedi.re.kr/inedx
# https://www.vworld.kr/dev/v4dv_geocoderguide2_s001.do

import folium

# 특정 학교의 위치에 마커를 표시 하는 처리

map = folium.Map(location=[37,127],zoom_start=7)

marker = folium.Marker([37.341435483, 126.733026596],
                    popup='한국공학대학교', 
                    icon = folium.Icon(color='blue'))

marker.add_to(map) 

map.save('uni_map.html')
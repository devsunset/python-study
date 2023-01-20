import pandas as pd
import folium

filePath = r'20.스타벅스 이디야 메가커피 위치 지도에 표시하기\스타벅스_이디야_메가커피_위치.xlsx'
df_from_excel = pd.read_excel(filePath)

매장_list = df_from_excel['매장'].to_list()
매장이름_list = df_from_excel['매장이름'].to_list()
좌표X_list = df_from_excel['좌표_X'].to_list()
좌표Y_list = df_from_excel['좌표_Y'].to_list()


map = folium.Map(location=[37,127],zoom_start=7)

for i in range(len(매장_list)):
    if "스타벅스" in 매장_list[i] :
        marker = folium.Marker([좌표Y_list[i],
                                좌표X_list[i]],
                                popup=매장이름_list[i], 
                                icon = folium.Icon(color='green'))
    elif "이디야" in 매장_list[i] :
        marker = folium.Marker([좌표Y_list[i],
                                좌표X_list[i]],
                                popup=매장이름_list[i], 
                                icon = folium.Icon(color='blue'))
    elif "메가커피" in 매장_list[i] :
        marker = folium.Marker([좌표Y_list[i],
                                좌표X_list[i]],
                                popup=매장이름_list[i], 
                                icon = folium.Icon(color='orange'))
    marker.add_to(map) 

map.save(r'20.스타벅스 이디야 메가커피 위치 지도에 표시하기/매장위치.html')
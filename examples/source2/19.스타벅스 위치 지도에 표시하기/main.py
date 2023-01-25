import pandas as pd
import folium

filePath = '스타벅스위치.xlsx'
df_from_excel = pd.read_excel(filePath)

name_list = df_from_excel['이름'].to_list()
position_x_list = df_from_excel['long'].to_list()
position_y_list = df_from_excel['lat'].to_list()

map = folium.Map(location=[37,127],zoom_start=7)

for i in range(len(name_list)):
    if "DT" in name_list[i] :
        marker = folium.Marker([position_y_list[i],
                                position_x_list[i]],
                                popup=name_list[i], 
                                icon = folium.Icon(color='black'))
    else:
        marker = folium.Marker([position_y_list[i],
                                position_x_list[i]],
                                popup=name_list[i], 
                                icon = folium.Icon(color='blue'))
    marker.add_to(map) 

map.save('star_map.html')
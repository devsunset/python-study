import folium

map = folium.Map(location=[37,127],zoom_start=7)

marker = folium.Marker([37.501087, 127.043069],
                    popup='역삼아레나빌딩', 
                    icon = folium.Icon(color='blue'))

marker.add_to(map) 

map.save(r'19.스타벅스 위치 지도에 표시하기/star_map.html')
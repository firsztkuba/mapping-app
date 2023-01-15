import folium
map = folium.Map(location=[54.33, 22.68], zoom_start=10, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="Mapa")
fg.add_child(folium.Marker(location=[54.328, 18.561], popup="Mieszkanko", icon=folium.Icon(color="gold")))
map.add_child(fg)

map.save("map1.html")
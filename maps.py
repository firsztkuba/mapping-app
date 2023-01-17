import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
longitude = list(data["LON"])
latitude = list(data["LAT"])

map = folium.Map(location=[54.33, 22.68], zoom_start=10, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="Mapa")
fg.add_child(folium.Marker(location=[54.328, 18.561], popup="Mieszkanko", icon=folium.Icon(color="gold")))
for lat, lon in zip(latitude, longitude):
    fg.add_child(folium.Marker(location=[lat, lon], popup="Volcanoe", icon=folium.Icon(color="red")))

map.add_child(fg)

map.save("map1.html")

print(latitude, longitude)
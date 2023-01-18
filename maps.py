import folium
import pandas

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s n.p.m.
"""

data = pandas.read_csv("Volcanoes.txt")
longitude = list(data["LON"])
latitude = list(data["LAT"])
names = list(data["NAME"])
elevation = list(data["ELEV"])
status = list(data["STATUS"])

def color_picker(value):
    if value < 2000:
        return "lightgreen"
    elif value < 3000:
        return "orange"
    else:
        return "darkred"

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="cartodb dark_matter")
fg = folium.FeatureGroup(name = "My Map")
 
for lt, ln, el, name in zip(latitude, longitude, elevation, names):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=7, popup=folium.Popup(iframe), fill_color=color_picker(el), color="grey", fill_opacity=0.8))
 
fg.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read()))

map.add_child(fg)

map.save("map1.html")

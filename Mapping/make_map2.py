import folium
map = folium.Map(location=[38.58, -99.09], zoom_start=6, titles="Strem Terrain")

fg = folium.FeatureGroup(name="My Map")

for coodinates in [[38.2, -99.1],[39.2, -97.1]]:
    fg.add_child(folium.Marker(location=coodinates, popup="Hi I am a marker", icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("Map2.html")
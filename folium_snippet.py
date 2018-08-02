"""
Folium is used to create interactive maps.
"""
import folium

mapOBJ = folium.Map(location=[39.5, -98.35], zoom_start=4, tiles='Stamen Terrain')
mapOBJ.save(outfile='map.html')
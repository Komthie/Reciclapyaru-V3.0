import folium
from folium.plugins import HeatMap

# Define your list of addresses (latitude, longitude)
locations = [
    [-28.9350, -49.4847],  # Address 1
    [-28.942484240022992, -49.469783790572585],  # Address 2
    [-28.946965996373297, -49.48046265826469],  # Address 3
    [-28.944153001837524, -49.459540794670964],  # Address 4
    [-28.93313867769802, -49.473815607580114],  # Address 5
    [-28.939246110150933, -49.486128962825056]  # Address 6
]

# Create the Folium map
mapa = folium.Map(location=[-28.9350, -49.4847], zoom_start=15)

# Create the heatmap with the list of locations and desired radius
heatmap = HeatMap(locations, radius=30).add_to(mapa)

# Save the map as "calor.html"
mapa.save("calor.html")
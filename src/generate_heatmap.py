import pandas as pd
import folium
from folium.plugins import HeatMap

df = pd.read_csv("../data/wifi_log.csv")

# Localização base (ex: Lisboa)
mapa = folium.Map(location=[38.7169, -9.1399], zoom_start=15)

# Exemplo: pontos fictícios com intensidade
heat_data = [[38.7169, -9.1399, row['RSSI']] for index, row in df.iterrows()]

HeatMap(heat_data).add_to(mapa)
mapa.save("../data/heatmap_wifi.html")

print("Heatmap gerado em data/heatmap_wifi.html")


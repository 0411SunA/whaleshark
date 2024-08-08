# 남규 :

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import folium


gsheet_url = "https://docs.google.com/spreadsheets/d/1McH-oBzPZ8ewfyEl605wq-9b3gZHCIIBVbWHEHwNnIs/gviz/tq?tqx=out:csv&sheet=ames-spot"

spot_loc = pd.read_csv(gsheet_url)


# 집위치 데이터 표시=============================================================
house_loc = pd.read_csv('data/house_loc.csv')

house_loc = house_loc.iloc[:, -2:]
map_sig = folium.Map(location = [42.034482, -93.642897],
                     zoom_start = 10,
                     tiles = 'cartodbpositron')

for i in range(2930):
  folium.Circle([house_loc.iloc[i,1], house_loc.iloc[i,0]],
                radius = 10, popup = str(i)).add_to(map_sig)
map_sig.save('map_ames.html')
#================================================================================


for i in range(2930):
  folium.Circle([house_loc.iloc[i,1], house_loc.iloc[i,0]],
                radius = 10, popup = str(i)).add_to(map_sig)
map_sig.save('map_ames.html')
spot_loc.iloc[:,2:]





















import folium
import streamlit as st
import pandas as pd
from streamlit_folium import st_folium

# Make an empty map
m = folium.Map(location=[3.8,101.8], tiles="OpenStreetMap", zoom_start=10,prefer_canvas = True)

df = pd.read_csv("data.csv")
# add marker one by one on the map
for i in range(0,len(df)):
    folium.Marker(
        location=[df.iloc[i]['lat'], df.iloc[i]['lon']],
        #popup=df.iloc[i]['name'],
    ).add_to(m)

# Show the map without markers
st_data = st_folium(m, width=725)
import folium
import streamlit as st

from streamlit_folium import st_folium

import folium

# Make an empty map
m = folium.Map(location=[20,0], tiles="OpenStreetMap", zoom_start=2)

# Show the map

st_data = st_folium(m, width=725)
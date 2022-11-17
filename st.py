import folium
import streamlit as st
import pandas as pd
from streamlit_folium import st_folium

# Make an empty map
m = folium.Map(location=[3.1,101], tiles="OpenStreetMap", zoom_start=20)

# Show the map

st_data = st_folium(m, width=725)
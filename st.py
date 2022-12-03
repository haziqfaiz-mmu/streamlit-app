import folium
import streamlit as st
import pandas as pd
#import altair as alt
from streamlit_folium import st_folium

# Make an empty map
m = folium.Map(location=[3.8,101.8], tiles="OpenStreetMap", zoom_start=10,prefer_canvas = True)
st.header('This is a header')
df = pd.read_csv("data.csv")

#test chart
# data = pd.DataFrame({'x': ['A', 'B', 'C', 'D', 'E'],
#                      'y': [5, 3, 6, 7, 2]})

# chart = alt.Chart(data).mark_bar().encode(
#     x='x',
#     y='y')
# add marker one by one on the map
for i in range(0,len(df)):
    folium.Marker(
        location=[df.iloc[i]['lat'], df.iloc[i]['lon']],
        # popup=folium.Popup(max_width=450).add_child(
        #     folium.VegaLite(chart, width=450, height=250))
    ).add_to(m)

# Show the map with markers
st_data = st_folium(m, width=725)


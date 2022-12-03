import folium
import pandas as pd
import altair as alt

center = [46.3014, -123.7390]

# Some random data that I like to plot in the popup.
data = pd.DataFrame({'x': ['A', 'B', 'C', 'D', 'E'],
                     'y': [5, 3, 6, 7, 2]})

chart = alt.Chart(data).mark_bar().encode(
    x='x',
    y='y')
m = folium.Map(location=center, zoom_start=13, tiles="Stamen Terrain")
folium.Marker(
    location=center,
    popup=folium.Popup(max_width=450).add_child(
        folium.VegaLite(chart, width=450, height=250)
    ),
).add_to(m)
m
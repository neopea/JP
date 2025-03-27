import streamlit as st
import folium
from tinydb import TinyDB, Query
from streamlit_folium import st_folium
from getloc import get_current_location
from database import restaurant_handler, con_handler

# Initialize the restaurant handler to access the database
handler = restaurant_handler()
conhandler = con_handler()

# Set page title
st.title("GPS Function with Restaurant and Convenience Store Icons")

user_location = get_current_location()  # Ensure this returns a tuple like (latitude, longitude)
# Create a folium map centered around the user's location
m = folium.Map(location=user_location, zoom_start=12)

# Fetch locations from the database
locations = handler.db.all()
loc = conhandler.db.all()



# Adding restaurant markers
for restaurant in locations:
    folium.Marker(
        location=restaurant["coordinates"],
        popup=f"{restaurant['restaurant_name']} - {restaurant['type']}. {restaurant['location']}",
        icon=folium.Icon(color='green', icon='utensils')  # Change icon color to green for restaurants
    ).add_to(m)

# Adding convenience store markers
for convenience_store in loc:
    folium.Marker(
        location=convenience_store["coordinates"],
        popup=f"{convenience_store['con_name']} -  {convenience_store['location']}",
        icon=folium.Icon(color='orange', icon='store')  # Change icon color to orange for convenience stores
    ).add_to(m)

# Render the map in Streamlit
st_data = st_folium(m, width=725, zoom=125)

# Optionally add further functionality, like user interaction or data filtering
st.write("Click on the markers to see more details.")
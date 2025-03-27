import streamlit as st
import folium
from streamlit_folium import st_folium


from getloc import get_current_location
from database import restaurant_handler

handler = restaurant_handler()
# Set page title
st.title("GPS Function with Restaurant and Convenience Store Icons")

# Get user's current location (for simplicity, let's use hardcoded coordinates)
# In a real application, you would probably use a GPS library or an API to get this information
user_location = (get_current_location())  # Example: New York City coordinates

# Create a folium map centered around the user's location
m = folium.Map(location=user_location, zoom_start=120)

#import data from other db later 
locations = {
    "Restaurants": [
        {"name": "Joe's Pizza", "coordinates": (40.731610, -73.935242)},
        {"name": "The Burger Joint", "coordinates": (40.732610, -73.938242)},
    ],
    "Convenience Stores": [
        {"name": "7-Eleven", "coordinates": (40.733610, -73.939242)},
        {"name": "Duane Reade", "coordinates": (40.734610, -73.940242)},
    ]
}

locations = handler.db.all()

# Add restaurant markers to the map
for restaurant in locations["Restaurants"]:
    folium.Marker(
        location=restaurant["coordinates"],
        popup=restaurant["name"],
        icon=folium.Icon(color='blue', icon='utensils')
    ).add_to(m)

# Add convenience store markers to the map
for store in locations["Convenience Stores"]:
    folium.Marker(
        location=store["coordinates"],
        popup=store["name"],
        icon=folium.Icon(color='green', icon='shopping-cart')
    ).add_to(m)

# Render the map in Streamlit
st_data = st_folium(m, width=725)

# Optionally add further functionality, like user interaction or data filtering
st.write("Click on the markers to see more details.")
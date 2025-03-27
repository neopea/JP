from database import restaurant_handler
import streamlit as st
from getloc import get_current_location
# Streamlit page title
st.title("Restaurant Data Collection")


RestHandler = restaurant_handler()
# Input fields for restaurant data
restaurant_name = st.text_input("Restaurant Name")
coordinates = get_current_location()
location = st.text_input("Location")
restaurant_type = st.selectbox("Restaurant Type", options = [
    "Mexican",
    "Thai",
    "Italian",
    "Chinese",
    "Indian",
    "Japanese",
    "French",
    "Mediterranean",
    "American",
    "Spanish"
])
# Submit button
if st.button("Add Restaurant"):
    if restaurant_name and coordinates and location and restaurant_type:
        RestHandler.add_record(restaurant_name, coordinates, location, restaurant_type)
    else:
        st.error("Please fill in all fields.")

# Optionally, show existing records
if st.button("Show All Restaurants"):
    records = RestHandler.db.all()
    if records:
        st.write(records)
    else:
        st.warning("No records found.")
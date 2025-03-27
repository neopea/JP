from database import con_handler
import streamlit as st
from getloc import get_current_location
# Streamlit page title
st.title("Store Data Collection")


RestHandler = con_handler()
# Input fields for restaurant data
restaurant_name = st.text_input("Store Name")
coordinates = get_current_location()
location = st.text_input("Location")

if st.button("Confirm"):
    if restaurant_name and coordinates and location :
        RestHandler.add_record(restaurant_name, coordinates, location)
    else:
        st.error("Please fill in all fields.")

# Optionally, show existing records
if st.button("Show All Stores"):
    records = RestHandler.db.all()
    if records:
        st.write(records)
    else:
        st.warning("No records found.")
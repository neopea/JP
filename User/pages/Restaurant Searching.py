import streamlit as st
from database import restaurant_handler
from geopy.distance import great_circle
from getloc import get_current_location

# Initialize the restaurant handler
my_handler = restaurant_handler()

# Streamlit app title
st.title("Restaurant Preference Selector")

# Price slider for selecting the price of food
price = st.select_slider("Select the price of the food ($)", options=range(1, 50), value=(20))

# Maximum distance slider for selecting the distance in kilometers
max_distance = st.select_slider("Select maximum distance (km)", options=range(1, 101), value=5)

# Options for filtering
categories = [
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
]
selected_types = st.multiselect("Select Food Categories", options=categories)

# Get the user's current location
user_location = get_current_location()  # Should return a tuple like (latitude, longitude)

# Fetch all restaurant data from the database
restaurants = my_handler.db.all()

# Filter restaurants based on user preferences
filtered_restaurants = []

if st.button("Confirm"):
    for i in range(len(restaurants)):
        restaurant = restaurants[i]
        # Check if the restaurant matches the selected types and price
        restaurant_categories = restaurant['type']

        # Calculate the distance from the user's location to the restaurant's location
        restaurant_location = restaurant['coordinates']  # Assume you have coordinates

        if restaurant_location:
            distance = great_circle(user_location, restaurant_location).km
        # Filtering logic
        if (distance <= max_distance and 
            (not selected_types or any(cat in restaurant_categories for cat in selected_types))):
            filtered_restaurants.append([restaurant , distance ])

    # Display the filtered results
    if filtered_restaurants:
        st.subheader("Filtered Restaurants:")
        for restaurant in filtered_restaurants:
            st.write(f"**{restaurant[0]['restaurant_name']}**")
            st.write("Rating " +  "⭐"* 5)
            st.write(f"Distance: {restaurant[1]:.2f} km")
            st.write(f"Categories: {(restaurant[0]['type'])}")
            st.write("---")  # Separator
    else:
        st.write("No restaurants found matching your criteria.")
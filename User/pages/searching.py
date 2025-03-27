import streamlit as st
from database import restaurant_handler
from geopy.distance import great_circle
from getloc import get_current_location
# Initialize the restaurant handler
my_handler = restaurant_handler()

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


# Streamlit app title
st.title("Restaurant Preference Selector")

# Price slider for selecting the price of food
price = st.select_slider("Select the price of the food ($)", options=range(1, 50), value=(20))

# Maximum distance slider for selecting the distance in kilometers
max_distance = st.select_slider("Select maximum distance (km)", options=range(1, 11), value=5)

# Multi-select for choosing food categories
selected_types = st.multiselect("Select Food Categories", options=categories)

# Button to submit and filter restaurants based on user's choices
from tinydb import TinyDB, Query

# Sample database setup (You should replace this with your actual database file)
db = TinyDB('restaurant.json')  

def find_restaurant(distance_limit, restaurant_type, user_location):
    Restaurant = Query()

    # Filter by restaurant type and price
    results = db.search(
        (restaurant_type in Restaurant.type) 
        #(Restaurant.price <= max_price)
    )

    suitable_restaurants = []

    for restaurant in results:
        # Calculate the distance to the restaurant
        restaurant_location = restaurant['coordinates']  # Assuming coordinates are in (latitude, longitude)
        distance = great_circle(user_location, restaurant_location).kilometers
        
        # Check if the distance is within the limit
        if distance <= distance_limit:
            suitable_restaurants.append(restaurant)

    return suitable_restaurants

# Example usage
user_location = get_current_location()  # Latitude and Longitude for New York City
distance_limit = 10  # in kilometers
restaurant_type = 'Italian'

suitable_restaurants = find_restaurant(distance_limit, restaurant_type,  user_location)


confirm = st.button("search")
if confirm :
    print('hi')
# Display suitable restaurants
for restaurant in suitable_restaurants:
    print(f"Restaurant Name: {restaurant['restaurant_name']}, Location: {restaurant['location']}, Distance: {great_circle(user_location, restaurant['coordinates']).kilometers:.2f} km")
import streamlit as st
from database import product_handler  # changed from restaurant_handler to food_handler
from geopy.distance import great_circle  # This import may no longer be necessary, but kept for possible future use
from getloc import get_current_location

# Initialize the food handler
my_handler = product_handler()  # Updated to food_handler

# Streamlit app title
st.title("Food Preference Selector")

# Price slider for selecting the price of food
price = st.slider("Select the maximum price of the food ($)", min_value=1, max_value=50, value=30)

# Options for filtering
categories = ["Fruits", "Vegetables", "Packaged food" ,"Bread" ,"Dairy" ,"Rice" ,"Drinks" ,"Noodles" ,"Others"]

selected_types = st.multiselect("Select Food Categories", options=categories)

# Fetch all food data from the database
foods = my_handler.db.all()  # Assuming the database method returns a list of food items

# Filter food items based on user preferences
filtered_foods = []

if st.button("Confirm"):
    for i in range(len(foods)):
        food = foods[i]
        # Check if the food matches the selected types and price
        food_categories = food['category']  # Access the category list
        food_price = food['price']  # Access the price

        # Filtering logic
        if food_price <= price and (not selected_types or any(cat in food_categories for cat in selected_types)):
            filtered_foods.append(food)

    # Display the filtered results
    if filtered_foods:
        st.subheader("Filtered Foods:")
        for food in filtered_foods:
            st.write(f"**{food['name']}**")
            st.write('Description:')
            st.write(food['description'])  # Show the description of the food
            st.write(f"Price: ${food['price']:.2f}")
            st.write(f"Available Quantity: {food['quantity_available']}")
            st.write(f"Categories: {[x for x in food['category']]}")
            st.write("---")  # Separator
    else:
        st.write("No foods found matching your criteria.")
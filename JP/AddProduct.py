import streamlit as st
from PIL import Image
from database import product_handler
# Set the title of the app
st.title("Upload and Save Image as food.jpg")
ProductHandler = product_handler()


# File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded file as an image
    image = Image.open(uploaded_file)
    
    # Display the image
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Save the image as food.jpg
    image.save("food123.jpg")
    st.success("Image saved as food.jpg")


st.title("Webcam Image Capture with Streamlit")

    # Use the camera input widget
camera_input = st.camera_input("Take a picture")

if camera_input:
    # Read the image as a PIL image
    image = Image.open(camera_input)

    # Save the image
    image.save("photo.jpg")
    
    # Display the captured image
    st.image(image, caption="Captured Image", use_column_width=True)
    st.success("Image saved as photo.jpg")

name = st.text_input("Supplier name and Food name")
description=st.text_area("Description")
image_path = "photo.jpg"  # Make sure to update this to a valid image path
expiration_date = str(st.date_input("Expiration date" ,value= None))
price= st.number_input("Price ($)", min_value=0.0, format="%.2f")
quantity_available=st.number_input("Quantity", min_value=0)
category= st.multiselect( # Multiple categories for the user to choose
"Choose the category of the food item" , 
["Fruits", "Vegetables", "Grain" ,"Protein" ,"Dairy" ,"Fats and Oils" ,"Drinks" ,"Snacks" ,"Others"]
)

confirm = st.button("Confirm")
if confirm:
    print("ejfefejhfnjefe")
    ProductHandler.add_product(
        name=name,
        description=description,
        image_path=image_path,
        expiration_date=expiration_date,
        price=price,
        quantity_available=quantity_available,
        category=category)
    st.success("Your product had been uploaded")

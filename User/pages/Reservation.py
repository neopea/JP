import streamlit as st
from database import order_handler , product_handler

OrderHandler = order_handler()
ProductHandler = product_handler()

x = ProductHandler.db.all()
food_li = []
for i in range(len(x)):
    y = x[i]
    food_li.append(y["name"])

name = st.selectbox("food selection" , options= food_li)

quantity = st.number_input("Quantity wanted" ,  min_value=1, max_value=x[food_li.index(name)]["quantity_available"]  , value=1, step=1, format='%d')




time = str(st.time_input("Pick Up time") )
date = str(st.date_input("Date"))


temp = date + "-"+time
confirm = st.button("Reserve the food")
if confirm:
    OrderHandler.add_record(name , quantity , temp)
    ProductHandler.update_product_quantity(name , -1 * quantity)
    st.success("Food Resevered")


import streamlit as st
from database import order_handler , product_handler

OrderHandler = order_handler()
ProductHandler = product_handler()

name = st.text_input("food selection")

quantity = st.number_input("Quantity wanted" ,  min_value=1, value=1, step=1, format='%d')




time = str(st.time_input("Pick Up time") )
date = str(st.date_input("Date"))


temp = date + time
confirm = st.button("Reserve the food")
if confirm:
    OrderHandler.add_record(name , quantity , temp)
    ProductHandler.update_product_quantity(name , -1 * quantity)
    st.success("Food Resevered")


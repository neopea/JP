import streamlit as st
from database import order_handler

handler= order_handler()



x = handler.db.all()
for i in range(len(x)):
    y = x[i]
    st.write(f"Required order of {y["name"]}")
    st.write(f"The quantity: {y["quantity"]}")
    st.write(f"The pick up time is {y["pick up time"]}")
    st.write("----")
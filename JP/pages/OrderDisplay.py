import streamlit as st
from database import order_handler

handler= order_handler()



if 'current_orders' not in st.session_state:
    st.session_state.current_orders = []

# Title of the application
st.title("Restaurant Order Management")

# Confirm order part
st.header("Current Orders")
if st.session_state.current_orders:
    for idx, order in enumerate(st.session_state.current_orders):
        st.write(f"{idx + 1}. {order['Quantity']} x {order['Food Type']} at ${order['Price']:.2f} each - Total: ${order['Total Price']:.2f}")

        if st.button(f"Confirm Order {idx + 1} Done"):
            st.session_state.current_orders.pop(idx)  # Remove the confirmed order
            st.success(f"Order {idx + 1} confirmed as done!")
            handler.update_product_quantity(product_name=order ,  )
else:
    st.write("No current orders.")

# Footer
st.write("---")
st.write("Add orders to the list to manage them.")
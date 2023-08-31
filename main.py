import streamlit as st

st.write("""
# Largest number identifier
This app identifies the largest of the given three numbers
""")

num_1 = st.number_input("Enter the first number",step=1)
num_2 = st.number_input("Enter the second number",step=1)
num_3 = st.number_input("Enter the third number",step=1)

if st.button('Find Largest'):
    st.write('Max is = ', max([float(num_1), float(num_2), float(num_3)]))  

        
        

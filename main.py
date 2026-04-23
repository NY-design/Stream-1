import streamlit as st
#Title of App
st.title("My First Streamlit App")

#Adding text
st.write("Hello! Creating a simple web application using stremlit library.")

# Take User Input
name=st.text_input("Enter your name")

#Display a message a button is clicked
if st.button("Submit"):
   st.write(f"Hello,{name}!Welcome to strem 1")

import streamlit as st
#Title of App
#st.title("My First Streamlit App")
st.title("Exam Score Predictor")
#Adding text
st.write("Hello! enter hours studies to predict the exam score.")

# Take User Input
#name=st.text_input("Enter your name")
hour=st.number_input("Enter age :")
#Display a message a button is clicked
if st.button("Predict Score"):
   st.write(f"Hello,{name}!Welcome to strem 1")

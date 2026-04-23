#import streamlit as st
#Title of App
#st.title("My First Streamlit App")
#st.title("Exam Score Predictor")
#Adding text
#st.write("Hello! enter hours studies to predict the exam score.")

# Take User Input
#name=st.text_input("Enter your name")
#hours=st.number_input("Enter age :")
#Display a message a button is clicked
#if st.button("Predict Score"):
 #  st.write(f"Hello,{hours}!Welcome to strem 1")
import streamlit as st

st.title("Exam Score Predictor")

st.write("Hello! Enter hours studied to predict the exam score.")

# Input
hours = st.number_input("Enter study hours:", min_value=0.0)

# Button
if st.button("Predict Score"):
    st.write(f"You entered: {hours} hours")

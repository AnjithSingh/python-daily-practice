import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlit text input')
name = st.text_input("Enter your name")

age = st.slider("Select Your Age :" , 0,100,25)

st.write(f"your age is : {age}")

options = ['Python','Js', 'Assemnly','Java']
choice = st.selectbox("choose your fav lang",options)
st.wrtie(choice)



if name:
    st.write(f"Hello , {name}")

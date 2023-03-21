# Importing Streamlit
import pandas as pd
import streamlit as st

# Tittle and sub tittle of the web form
st.set_page_config(layout="centered", page_icon="📖", page_title="Newsletter registration")
st.title("📖 Newsletter registration")
st.subheader("The main informations about Tech twice a week!")

# Parameters for tto get the information
with st.form("Register", clear_on_submit=True):
    name = st.text_input("Enter your full name")
    college = st.text_input("Where do you study?")
    course = st.text_input("What is your field of study?")
    email = st.text_input("What is your best email?")
    submit = st.form_submit_button("I want to get connected")

    if submit:
        print(name)

# To run the code -> streamlit run NewsletterHomePage.py
print(email)


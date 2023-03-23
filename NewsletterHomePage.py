# Importing Streamlit
import pandas as pd
import streamlit as st
import pyodbc

# Creating a new connection to a LOCAL DB
conn_str = ("Driver={SQL Server};"
            "Server=MAIALAPTOP;"
            "Database=newsletter;"
            "Trusted_Connection=yes;"
            "Uid=auth_window")
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Tittle and sub tittle of the web form
st.set_page_config(layout="centered", page_icon="📖", page_title="Newsletter registration")
st.title("📖 Newsletter registration")
st.subheader("The main informations about Tech twice a week!")

# Parameters for tto get the information
with st.form(key="Register", clear_on_submit=True):
    firstname = st.text_input("Enter your first name")
    lastname = st.text_input("Enter your last name")
    college = st.text_input("Where do you study?")
    course = st.text_input("What is your field of study?")
    email = st.text_input("What is your best email?")
    submit_register = st.form_submit_button("I want to get connected")

# Creating lists and dictionaries to insert the new data
    if submit_register:
        dfUsers = pd.DataFrame({"Name": [firstname], "Last Name": [lastname],
                                "College": [college], "Course": [course], "Email": [email]})
        st.success("Your registration is complete {}".format(firstname))
        st.balloons()
        # Execute the query
        cursor.execute("INSERT INTO Register (FirstName, LastName, College, Course, Email) VALUES (?, ?, ?, ?, ? )",
                       (firstname, lastname, college, course, email))

        # the connection is not autocommited by default. So we must commit to save our changes.
        conn.commit()
        print(dfUsers)

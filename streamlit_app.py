import streamlit as st
import mysql.connector
import pandas as pd

# Database Connection

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="OrganDonationDB"
)

# Page Title

st.title("Organ Donation and Transplant Matching System")

# Sidebar

option = st.sidebar.selectbox(
    "Select Option",
    ["Donors", "Recipients", "Hospitals", "Transplants"]
)

# Donor Page

if option == "Donors":

    query = "SELECT * FROM Donors"

    data = pd.read_sql(query, conn)

    st.subheader("Donor Records")

    st.dataframe(data)

# Recipient Page

elif option == "Recipients":

    query = "SELECT * FROM Recipients"

    data = pd.read_sql(query, conn)

    st.subheader("Recipient Records")

    st.dataframe(data)

# Hospital Page

elif option == "Hospitals":

    query = "SELECT * FROM Hospitals"

    data = pd.read_sql(query, conn)

    st.subheader("Hospital Records")

    st.dataframe(data)

# Transplant Page

elif option == "Transplants":

    query = "SELECT * FROM Transplants"

    data = pd.read_sql(query, conn)

    st.subheader("Transplant Status")

    st.dataframe(data)

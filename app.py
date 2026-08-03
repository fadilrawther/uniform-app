import streamlit as st
import gspread
from google.oauth2.service_account
import Credentials
#connect to google sheets
scope=
["https://www.googleapis.com/auth/spreadsheets"]

creds=
Credentials.from_service_account_info(
    "st.secrets["gcp_service_account"],
    scope=scope
)    
client=gspread.authorize(creds)

sheet=client.open("Client Data").sheet1
#UI
st.title("MIHANIYY School Uniform Form")
school=st.text_input("School Name")
class_name=st.text_input("Class")
uniform=st.selecttbox("Uniform Type",["Shirt","T-Shirt"])
bottom=st.selectbox("Bottom Type",["Shorts","Pants"])
colour=st.selectbox("colour",["Red","Blue","Green","Yellow"])
size=st.selectbox("Size",["XS","S","M","L","XL","XXL","3XL","5XL"])
qty=st.number_input("Quantity",min_value=1)
#submit
if st.button("Submit Order"):
    sheet.append_row([
        school,
        class_name,
        uniform,
        bottom,
        colour,
        size,
        qty
    ])
    st.success("Order submitted successfully!")


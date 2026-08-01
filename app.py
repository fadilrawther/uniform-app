import streamlit as st
import csv

st.title("Uniform order Form")

name=st.text_input("Name")
phone=st.text_input("Phone")
quantity=st.number_input("Quantity",min_value=1)

if st.button("Submit"):
    with open("Orders.csv","a", newline="")as f:
        writer=csv.writer(f)
        writer.writerow([name,phone,quantity])
        st.success("Ordersubmitted!")

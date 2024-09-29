import streamlit as st
st.title("Tip Calculator")

Bill = st.number_input("What was the total Bill amount? ")
Tip = st.number_input("How much tip would you like to give? ", min_value = 0.0, format = "%.2f")
Split = st.number_input("How many people to split the bill? (atleast 1)", min_value = 1)
total = (Bill + Tip)/Split

st.write(f"Each person should pay : " + {total})
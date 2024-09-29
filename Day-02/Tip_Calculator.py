import streamlit as st

st.title("Tip Calculator")

# Get inputs
Bill = st.number_input("What was the total Bill amount?", value=0.0, format="%.2f")
Tip = st.number_input("How much tip would you like to give?", min_value=0.0, value=0.0, format="%.2f")
Split = st.number_input("How many people to split the bill? (at least 1)", min_value=1, value=1)

# Calculate total payment per person
if Split > 0:  # Although it's redundant here due to the input restrictions
    total = (Bill + Tip) / Split
    st.write(f"Each person should pay: {total:.2f}")
else:
    st.write("Please enter a valid number of people.")

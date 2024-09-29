import streamlit as st

# Display a welcome message
st.title("Band Name Generator")

# Take user inputs for the city and pet name
city = st.text_input("What's the name of the city you grew up in?")
pet = st.text_input("What's your pet's name?")

# Generate the band name when both inputs are provided
if city and pet:
    st.write("Your band name could be " + city + " " + pet)
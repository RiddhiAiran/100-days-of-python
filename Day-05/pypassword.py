import random
import streamlit as st

# Define character sets
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['!', '#', '$', '%', '^', '&', '*', '(', ')', '@']

# Streamlit App UI
st.title("💻 Your Password Generator 💻")

# Input from the user
user_abc = st.number_input("How many letters would you like in your password?", min_value=0, max_value=50)
user_num = st.number_input("How many numbers would you like in your password?", min_value=0, max_value=50)
user_spe = st.number_input("How many special characters would you like in your password?", min_value=0, max_value=50)

# Button to generate password
if st.button("Generate Password"):
    password = []

    # Add random letters
    for i in range(user_abc):
        password.append(random.choice(alphabets))

    # Add random numbers
    for i in range(user_num):
        password.append(random.choice(digits))

    # Add random special characters
    for i in range(user_spe):
        password.append(random.choice(special))

    # Shuffle the password list
    random.shuffle(password)

    # Create final password string manually
    final_password = ""
    for char in password:
        final_password += char

    # Display the generated password
    st.success(f"Your password is: {final_password}")

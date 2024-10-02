import random
import streamlit as st

# ASCII Art for Rock, Paper, Scissors
rock = '''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

items = [rock, paper, scissors]

# Streamlit UI
st.title("Rock, Paper, Scissors Game")

# User choice with a dropdown menu
user_choice = st.selectbox("What do you choose?", ["Rock", "Paper", "Scissors"])

# Convert user choice to corresponding index
user = ["Rock", "Paper", "Scissors"].index(user_choice)

if st.button("Play!"):
    # Display user's choice
    st.write(f"You chose: {user_choice}")
    st.code(items[user])  # Display ASCII art for user's choice

    # Computer's random choice
    computer = random.randint(0, 2)
    computer_choice = ["Rock", "Paper", "Scissors"][computer]

    # Display computer's choice
    st.write(f"Computer chose: {computer_choice}")
    st.code(items[computer])  # Display ASCII art for computer's choice

    # Determine the winner
    if user == computer:
        st.write("It's a Tie!")
    elif (user == 2 and computer == 1) or (user == 1 and computer == 0) or (user == 0 and computer == 2):
        st.write("You win!")
    else:
        st.write("Computer wins!")

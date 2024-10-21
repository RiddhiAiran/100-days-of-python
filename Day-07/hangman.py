import streamlit as st
import random

# Initialize session state variables to keep track of game state
if 'chosen_word' not in st.session_state:
    st.session_state.chosen_word = random.choice(['banboon', 'camel', 'hat', 'horse', 
                                                  'apple', 'sheep', 'friendship', 'mermaid'])

if 'lives' not in st.session_state:
    st.session_state.lives = 0

if 'correct_letters' not in st.session_state:
    st.session_state.correct_letters = []

if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Hangman ASCII art stages
stages = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========='''
]

# Function to display the current state of the word with guessed letters
def get_display_word():
    display = ''
    for letter in st.session_state.chosen_word:
        if letter in st.session_state.correct_letters:
            display += letter
        else:
            display += '_'
    return display

# Streamlit UI components
st.title("Hangman Game")

# Display the word with blanks for unguessed letters
st.subheader("Guess the Word:")
st.text(get_display_word())

# Display the current Hangman stage based on incorrect guesses
st.text(stages[st.session_state.lives])

# Input field for guessing a letter
if not st.session_state.game_over:
    guess = st.text_input("Enter a letter:").lower()

    if st.button("Submit Guess"):
        if guess in st.session_state.chosen_word:
            if guess not in st.session_state.correct_letters:
                st.session_state.correct_letters.append(guess)
                st.success(f"Correct! '{guess}' is in the word.")
            else:
                st.warning(f"You already guessed '{guess}'.")
        else:
            st.session_state.lives += 1
            st.error(f"Wrong guess! '{guess}' is not in the word.")

        # Check for game over conditions
        if '_' not in get_display_word():
            st.session_state.game_over = True
            st.success("Congratulations! You won!")
        elif st.session_state.lives == 6:
            st.session_state.game_over = True
            st.error(f"Game Over! The word was '{st.session_state.chosen_word}'.")

# Restart button
if st.session_state.game_over:
    if st.button("Restart Game"):
        # Reset all session state variables for a new game
        st.session_state.chosen_word = random.choice(['banboon', 'camel', 'hat', 'horse', 
                                                      'apple', 'sheep', 'friendship', 'mermaid'])
        st.session_state.lives = 0
        st.session_state.correct_letters = []
        st.session_state.game_over = False

import streamlit as st

# Initialize session state for game progression
if 'step' not in st.session_state:
    st.session_state.step = 1

# Display the game title and intro
st.title("🏝️ Treasure Island Adventure")

ascii='''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     "=.|                  |
|___________________|__"=._o"-._        "=.______________|___________________
          |                "=._o"=._      _"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; "=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .  ` ,  "-._"-._   ". '__|___________________
          |           |o"=._ , " ; .". ,  "-._"-._; ;              |
 _________|___________| ;-.o"=._; ."  '."\ . "-._ /_______________|_______
|                   | |o;    "-.o"=._`  ' " ,__.--o;   |
|___________________|_| ;     (#) -.o "=._.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      ".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
'''
st.code(ascii)

st.header("Welcome to Treasure Island! Your mission is to find the treasure.")

# Step 1: Crossroad
if st.session_state.step == 1:
    st.write("You're at a crossroad. Where do you want to go?")
    road = st.selectbox("Choose a direction:", ['Left', 'Right'])

    if st.button("Proceed"):
        if road.lower() == "left":
            st.session_state.step = 2  # Move to next step (Lake)
        else:
            st.error("You fell into a hole! 🕳️ Game Over.")
            st.session_state.step = 1  # Restart the game

# Step 2: Lake
if st.session_state.step == 2:
    st.write("You've come to a lake. There is an island in the middle of the lake.")
    lake = st.selectbox("What will you do?", ['Wait for a boat', 'Swim across'])

    if st.button("Next"):
        if lake.lower() == "wait for a boat":
            st.session_state.step = 3  # Move to next step (House)
        else:
            st.error("You were attacked by trout! 🐟 Game Over.")
            st.session_state.step = 1  # Restart the game

# Step 3: House with doors
if st.session_state.step == 3:
    st.write("You have arrived at the island unharmed. There is a house with 3 doors.")
    door = st.selectbox("Which door will you choose?", ['Red', 'Yellow', 'Blue'])

    if st.button("Open the door"):
        if door.lower() == "yellow":
            st.success("Congrats! You found the treasure! 🏆")
            st.session_state.step = 1  # Restart the game
        elif door.lower() == "red":
            st.error("Burned by fire! 🔥 Game Over.")
            st.session_state.step = 1  # Restart the game
        elif door.lower() == "blue":
            st.error("Eaten by beasts! 🐺 Game Over.")
            st.session_state.step = 1  # Restart the game
        else:
            st.error("Game Over!")
            st.session_state.step = 1  # Restart the game

import streamlit as st
import random
import time

# Title of the app
st.title("🎲 Creative Coin Toss Game 🪙")
st.write("Flip a coin and see if it's heads or tails!")

# Load images for heads and tails (replace with your image URLs or file paths)
coin_flip_gif = "https://cdn.dribbble.com/users/12524477/screenshots/18860746/media/34c431d2ce3d5d9734c1b8ffac98a698.gif"
heads_image = "https://w7.pngwing.com/pngs/257/577/png-transparent-round-silver-colored-1-indian-rupee-coin-udaipur-battle-of-haldighati-mewar-one-rupee-coin-india-akbar-udai-singh.png"  # Replace with actual image URL/path
tails_image = "https://www.vhv.rs/dpng/d/256-2560252_coin-png-pic-head-and-tail-of-indian.png"

# Function to simulate the coin flip
def flip_coin():
    # Show the animated coin flip GIF
    st.image(coin_flip_gif, width=200)
    
    # Wait for the duration of the GIF animation (adjust as per the length of your GIF)
    time.sleep(2)  # 2 seconds is just an example; match this to your GIF duration

# Button to start the coin toss
if st.button("Toss the Coin 🪙"):
    st.write("Tossing the coin...")

    # Run the coin flip animation
    flip_coin()

    # Final coin toss result
    result = random.choice(["Heads", "Tails"])

    # Display the result with corresponding image
    if result == "Heads":
        st.image(heads_image, width=200)
        st.write("🎉 It's **Heads**! 🎉")
    else:
        st.image(tails_image, width=200)
        st.write("🎉 It's **Tails**! 🎉")
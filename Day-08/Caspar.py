import streamlit as st

# List of alphabets
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
             'y', 'z']

def caesar(direction, text, shift):
    def encrypt(text, shift):
        encoded_text = ''
        for letter in text:
            if letter in alphabets:  # Check if letter is in alphabets
                new_index = alphabets.index(letter) + shift
                new_index %= len(alphabets)
                encoded_text += alphabets[new_index]
            else:
                encoded_text += letter  # Keep non-alphabet characters unchanged
        return encoded_text

    def decrypt(text, shift):
        decoded_text = ''
        for letter in text:
            if letter in alphabets:  # Check if letter is in alphabets
                new_index = alphabets.index(letter) - shift
                new_index %= len(alphabets)
                decoded_text += alphabets[new_index]
            else:
                decoded_text += letter  # Keep non-alphabet characters unchanged
        return decoded_text

    if direction == "encode":
        return encrypt(text=text, shift=shift)
    elif direction == "decode":
        return decrypt(text=text, shift=shift)
    else:
        return "Enter Valid Values"

# Streamlit UI
st.title("Caesar Cipher Encoder/Decoder")

# Input for direction
direction = st.radio("Choose an option:", ("encode", "decode"))

# Input for text message
text = st.text_area("Type your message:")

# Input for shift number
shift = st.number_input("Type the shift number:", min_value=1, max_value=25, value=1)

# Button to perform the operation
if st.button("Submit"):
    result = caesar(direction=direction, text=text.lower(), shift=shift)
    st.write("Result:", result)

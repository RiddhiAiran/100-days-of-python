import random 

words_list = ['apple', 'grapes', 'car', 'hat', 'google', 'interview', 'selected', 'Done']

word = random.choice(words_list)
placeholder = "_ " * len(word)
print(placeholder)

display = ''

lives = 4
while lives != 0 or word != display:
    guess = input("Guess a word! : ").lower()
    for letter in word:
        if letter == guess:
            display += letter
            print(display)
            lives -= 1
        else:
            print("Wrong! Try again")
            display += "_"
            lives -= 1

print(display)
import random

word_list = ['Banboon', 'camel', 'Hat', 'Horse', 'apple','sheep','friendship','marmaid']

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess the word letters : ").lower()

for i in chosen_word:
    if i == guess:
        print("Right")
    else:
        print("Wrong")
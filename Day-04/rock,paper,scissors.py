import random

rock = ""


paper = ""


scissors = ""

user_input = input("What do you choose? Type 0 for Rock, 1 for paper and 2 for scissors\n")

computer = random.randint(0,2)
print(f"Computer chose : {computer}")
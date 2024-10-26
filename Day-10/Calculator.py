import os

def clear_screen():
    os.system('clear')



def add(num_1, num_2):
    return num_1 + num_2

def sub(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

operations = {
    '+' : add,
    '-' : sub,
    '*' : multiply,
    '/' :divide
}

def Calculator():
    clear_screen()
    status = True
    num_1 = float(input("What's the first number : "))
    while status:
        for operators in operations:
            print(operators)
        operator = input("Pick an Operator : ")
        num_2 = float(input("What's the Next Number : "))
        answer = operations[operator](num_1,num_2)
        print(f'{num_1} {operator} {num_2} = {answer}')
        choice = input(f"Type 'y'to continue calculating with {answer}, or Type 'no' to start a new calculation \n").lower()
        if  choice == 'y':
            num_1 = answer
        else:
            status = False
            Calculator()
    
Calculator()
            
    


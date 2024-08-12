# Importing ramdom module
import random

# Defining choices list
choices = ['Rock', 'Paper', 'Scissor']

# using choice method from random module to pick any random choice from the given list
computer_choice = random.choice(choices)

# Taking input from user [Case Sensitive]
user_choice = input('Enter your choice [Rock/Paper/Scissor] = ')

# use this if you want to check the computer choice for testing purpose
# print(computer_choice)

# Applying conditions
if user_choice == computer_choice:
    print('Match Tie!')

elif user_choice == 'Rock':
    if computer_choice == 'Paper':
        print("Computer Won! Paper covers Rock")
    else:
        print('You won! Rock smashes scissor!')

elif user_choice == 'Paper':
    if computer_choice == 'Rock':
        print("You Won! Paper covers Rock")
    else:
        print('Computer won! Scissor cuts paper!')

elif user_choice == 'Scissor':
    if computer_choice == 'Paper':
        print("You Won! Scissor cut Paper")
    else:
        print('Computer won! Rock smashes Scissor!')
else:
    print('Invalid Choice')

# Developed By - Manish Kumar (https://github.com/halochaudhary)
# Give star if you like this simple rock paper scissor game

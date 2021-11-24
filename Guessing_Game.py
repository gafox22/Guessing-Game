import random
import sys

user_number = input("Please enter a random number between 1 and 10: ")
user_number = int(user_number)

if user_number <= 0 and user_number >= 11:
    print("You have entered an invalid value. Please try again")
    sys.exit()
    

def computer_guess():
    guess_1 = random.randint(1, 10)
    return "Is ",guess_1, " your number?"

print(computer_guess())

user_response = input("Y or N ")
user_resp = str(user_response)

if user_response == "N":
    print("Dang Nabbit!")
    print(computer_guess())
    user_response
if user_response == "Y":
    print("I knew it!!")


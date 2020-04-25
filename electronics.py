#MILK THOMAS

import sys
import random
yes_no= ["yes", "no"]
r_p_s= ["rock", "paper", "scissors"]

def get_input():
    print("Enter rock, paper, or scissors:" , end="")
    user_input = input()
    if user_input in r_p_s:
        return user_input
    else:
        print("Error")
        main()

def comp_input(): 
    numb= comp_numb()
    if numb == 1:
        return("rock")
    elif numb == 2:
        return("paper")
    else: 
        return("scissors")
def comp_numb():
    numb = random.randint(1,3)        
    return(numb)

def tie():
    print("Tie")

def win():
    print("You win!")

def lose():
    print("You lost you fucking idiot")

def play_again():
    second_input= ""
    while second_input not in yes_no:
        print("\n\nWould you like to play again? Type [yes] or [no]:" , end="")
        second_input = input()
    return second_input
       

def question(replay):
    if replay == "yes":
        main()
    if replay == "no":
        sys.exit(0) 

def game(user_input, computer_input):
    print("You said:" , end="")
    print(user_input)
    print("They said:" , end="")
    print(computer_input)
    if user_input == computer_input:
        tie()
    elif user_input == "rock" and computer_input == "scisscors":
        win()
    elif user_input == "rock" and computer_input == "paper":
        lose()
    elif user_input == "paper" and computer_input == "rock":
        win()
    elif user_input == "paper" and computer_input == "scisscors":
        lose()
    elif user_input == "scissors" and computer_input == "paper":
        win()
    else: 
        lose()

def main():
    user_input = get_input()
    computer_input= comp_input()
    game(user_input, computer_input)
    replay = play_again()
    question(replay)

main()
    
        
    

    

    



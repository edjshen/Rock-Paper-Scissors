# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def main():
    import random
    import time
    #initiate variables
    valid = 0
    user = 0
    pc = 0
    computerChoice = 0
    computerList = ["Rock","Paper","Scissors"]
    numbersList = [0,1,2]
    possible = {0:0,1:1,2:2,0:2,1:0,2:1}
    #introduction text
    print("Welcome to the Rock Paper Scissors Dojo \n")
    time.sleep(1)
    print("Rock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissors")
    time.sleep(1)
    print("Shoot!")
    time.sleep(1)
    #user input validation along with variable assingment
    userChoice = input("Please select your move \n")
    while(valid == 0):
        if(userChoice == "Rock" or userChoice == "rock" or userChoice == "ROCK"):
            print("You have chosen " + userChoice +"\n")
            valid = 1
            user = 0
        elif(userChoice == "Paper" or userChoice == "paper" or userChoice == "PAPER"):
            print("You have chosen " + userChoice +"\n")
            valid = 1
            user = 1
        elif(userChoice == "Scissors" or userChoice == "scissors" or userChoice == "SCISSORS"):
            print("You have chosen " + userChoice +"\n")
            valid = 1
            user = 2
        else:
            print("You have chosen " + userChoice +"\n")
            userChoice = input("Please input a valid selection \n")
            valid = 0
    #simulate random choice for computer
    pc = random.choice(numbersList)
    computerChoice = computerList[pc]
    print("The computer has chosen " + computerChoice + "\n")
    #indexing to find out who wins
    if user == pc:
        print("It is a tie")
    elif possible[user] == pc:
        print("You win!")
    elif possible[pc] == user:
        print("You lose :(")
    else:
        print("You broke the game")
        print("user" + str(user))
        print("pc"+ str(pc))
    print("\nThanks for playing!")
    
main()
    




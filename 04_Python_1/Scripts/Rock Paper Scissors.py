import random
#Creating a function that takes and verifies user's input
def verify_input():
    user = input("Type 'rock', 'paper' or 'scissors' or one of the letters 'r', 'p' or 's'\n")
    while True:
        if user == "rock" or user == "paper" or user == "scissors" or user == "Rock" or user == "Paper" or user == "Scissors" or user == "r" or user == "p" or user == "s" or user == "R" or user == "P" or user == "S":   
            return user 
        else:       
            user = input("This is not a valid value.\nType 'rock', 'paper', or 'scissors' or one of the letters 'r', 'p' or 's'\n")
#Function that generates a random choice from a list as a computer's move, prints it and returns it
def computer_choice():
    rps = ["rock", "paper", "scissors"]
    com = random.choice(rps)
    print(com)
    return com
#Function that checks for all the possible winning conditions for each side and returns the score for each round
def winning(user, com):
    user_wins = 0
    com_wins = 0

    if user == "rock" or user == "Rock" or user == "R" or user == "r":
        if com == "scissors":
            user_wins += 1
        elif com == "paper":
            com_wins += 1

    elif user == "paper" or user == "Paper" or user == "P" or user == "p":
        if com == "rock":
            user_wins += 1
        elif com == "scissors":
            com_wins += 1

    elif user == "scissors" or user == "Scissors" or user == "S" or user == "s":
        if com == "rock":
            com_wins += 1
        elif com == "paper":
            user_wins += 1

    return user_wins, com_wins
#Function that takes the score for each round, counts the total for each side and returns it
def score_tracker(user_wins, com_wins):
    user_count = 0
    com_count = 0
    if user_wins > com_wins:
        user_count += 1
    elif user_wins < com_wins:
        com_count += 1

    return user_count, com_count
#Function that starts the game and contains all the other functions. 
#Here we set the number of the rounds using a loop
#We also declare a winning case or a tie
def game():
    user_count = 0
    com_count = 0
    round = 0
    while round < 5:
        user = verify_input()
        com = computer_choice()
        user_wins, com_wins = winning(user, com)
        score_tracking = score_tracker(user_wins, com_wins)
        user_count += score_tracking[0]
        com_count += score_tracking[1]
        round += 1
    print(user_count, com_count)
    if user_count < com_count:
        print("Computer wins! You suck!")
    elif user_count > com_count:
        print("You win! Computer never sucks!")
    else:
        print("It's a tie! Go think of some other way to settle this down.")
#Starting the game by calling the mother function and restarting it if the user wishes so
game()
while True:
    restart = input("Not convinced? Play again! Type 'yes' or 'no'\n")
    if restart == "yes" or restart == "Yes" or restart == "y" or restart == "Y":
        game()
    elif restart == "no" or restart == "No" or restart == "n" or restart == "N":
        break
    else:
        print("This is not a valid entry!")



      
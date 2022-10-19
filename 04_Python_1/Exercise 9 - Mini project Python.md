# [Mini project Python]

[Creating three little terminal-games using Python.]

## Key terminology

[]

## Exercise

1. The code for the number gussing game goes as follows:

~~~
import random
#Making the game in a function so that we can restart it easily
def game():
    #Generating the random number
    x = random.randint(1,100)
    #Taking user's input
    y = input("Guess the number between 1 and 100\n")
    #Converting the (the string by default) input to an integer to be comparable with the generated random number
    y = int(y)
    #Checking if the input is between 1 and 100, if not we prompt the user once again and repeat that until we get a valid input
    while y > 100 or y < 1:
            y = input("Please enter a number between 1 and 100!\n")
            y = int(y)
    #Comparing the users input with the random number in a "while True" loop that only breaks when the input = the random number
    while True:
            if y == x:
                print("That's true! The number is " + str(x))
                break
            elif y < x:
                y = input("Try higher. Don't be afraid!\n")
                y = int(y)
                continue
            else:
                y = input("Try lower. Don't be so greedy!\n")
                y = int(y)
                continue
#Calling the game function
game()
#Checking if the user wants to play again, if yes calling the game function again and if no breaking
while True:
    restart = input("Play again? Type 'yes' or 'no'\n")
    if restart == "yes" or restart == "Yes" or restart == "y" or restart == "Y":
        game()
    elif restart == "no" or restart == "No" or restart == "n" or restart == "N":
        break
    else:
        print("This is not a valid entry!")
~~~

2. The code for Rock Paper Scissors goes as follows:

~~~
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
~~~

3_1. The code for Tic Tac Toe the multi-players version goes as follows:

~~~
#Creating a dict that maps the numbers of the squares and assign empty strings
#as values. The strings will be filled with the X's and O's
theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }
#This (initially) empty list where we append the keys of the dict will come in handy
#when we need to empty the string values of the dict to restart the game
board_keys = []
for key in theBoard:
    board_keys.append(key)
#Function that draws the game's board
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
#The main function of the game
def game():
    #Game starts always with X
    turn = 'X'
    count = 0
    #Prompting user's input as a square's number, checking if it's valid and assigning
    # the user's symbol (X or O) as a value to the key with the same number as the input
    # in the dict. In other words; filling the square with that number with X or O 
    for i in range(10):
        printBoard(theBoard)
        print("It's " + turn + "'s. Choose square number")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            while True:
                printBoard(theBoard)
                print("That square is already taken.\nChoose square number")
                new_attempt = input()
                if theBoard[new_attempt] == ' ':
                    move = new_attempt
                    theBoard[move] = turn
                    count += 1
                    break
                else:
                    continue
        #Checking for all possible winning conditions since round 5 (The least number of rounds a winning case can occur).        
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
        #If it's 9 rounds already and we still have no winner, that means it's a tie!        
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!")
        #Changing the turn after each round
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    #Restarting the game if the users wish so by calling the function from within
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        game()
#Calling the game function
game()
~~~

3_2. The code for Tic Tac Toe the single-player version goes as follows:

~~~
#The same code as for the multi-players version, except for some
#changes that I'll point out in comments along the way
import random

theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }
board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 'X'
    count = 0
    #User is X and computer is O. We only take user's input if it's X's turn
    for i in range(10):
        if turn == 'X':
            printBoard(theBoard)
            print("You're X. It's your turn. \nChoose square number")
            move = input()        
            if theBoard[move] == ' ':
                theBoard[move] = turn
                count += 1
            else:
                while True:
                    printBoard(theBoard)
                    print("That square is already taken.\nChoose square number")
                    new_attempt = input()
                    if theBoard[new_attempt] == ' ':
                        move = new_attempt
                        theBoard[move] = turn
                        count += 1
                        break
                    else:
                        continue
        #And if it's computer's turn, we generate a random number between 1 and 9
        # and check if it's not an already taken square. When valid we assign 
        # O as a value and fill the square            
        else:
            move = random.randint(1,9)
            move = str(move)
            if theBoard[move] == ' ':
                 theBoard[move] = turn
                 count += 1
            else:
                while True:
                    new_attempt = random.randint(1,9)
                    new_attempt = str(new_attempt)
                    if theBoard[new_attempt] == ' ':
                        move = new_attempt
                        theBoard[move] = turn
                        count += 1
                        break
                    else:
                        continue

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        if count == 9:
            printBoard(theBoard)
            print("\nGame Over.\n")
            print("It's a Tie!")

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'
    
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        game()
game()
~~~

### Sources

[1. <https://realpython.com/python-rock-paper-scissors/>

2. <https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874>]

### Overcome challenges

[]

### Results

[Script Number guessing](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/7b968e2925aa6dd8b91715c348d2485fb5b3acfd/04_Python_1/Scripts/Number%20guessing.py)  
[Script Rock Paper Scissors](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/7b968e2925aa6dd8b91715c348d2485fb5b3acfd/04_Python_1/Scripts/Rock%20Paper%20Scissors.py)  
[Script Tic Tac Toe - Multi-players](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/7b968e2925aa6dd8b91715c348d2485fb5b3acfd/04_Python_1/Scripts/Tic%20Tac%20Toe_Multi.py)  
[Script Tic Tac Toe - single-player](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/7b968e2925aa6dd8b91715c348d2485fb5b3acfd/04_Python_1/Scripts/Tic%20Tac%20Toe_Single.py)

![Number_guessing](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/86fa3eff36f33fee517a565c67f10ea4ac82467c/00_includes/Python/Number_guessing.png)
![RPS](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/86fa3eff36f33fee517a565c67f10ea4ac82467c/00_includes/Python/RPS.png)
![TTT](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/86fa3eff36f33fee517a565c67f10ea4ac82467c/00_includes/Python/TTT.png)

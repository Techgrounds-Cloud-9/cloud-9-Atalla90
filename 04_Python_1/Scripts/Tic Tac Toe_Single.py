#The same code as for the multi-players version, except for some
#changes that I'll point out in comments to along the way
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
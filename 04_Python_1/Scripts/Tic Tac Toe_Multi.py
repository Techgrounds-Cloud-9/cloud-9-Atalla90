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
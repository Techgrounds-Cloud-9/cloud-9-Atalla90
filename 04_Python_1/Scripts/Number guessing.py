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


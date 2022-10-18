import random

def game():
    x = random.randint(1,100)
    y = input("Guess the number between 1 and 100\n")
    y = int(y)

    while y > 100 or y < 1:
            y = input("Please enter a number between 1 and 100!\n")
            y = int(y)

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

game()
while True:
    restart = input("Play again? Type 'yes' or 'no'\n")
    if restart == "yes" or restart == "Yes" or restart == "y" or restart == "Y":
        game()
    elif restart == "no" or restart == "No" or restart == "n" or restart == "N":
        break
    else:
        print("This is not a valid entry!")


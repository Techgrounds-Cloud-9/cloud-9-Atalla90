while True:
    num = input("Hit me with a num: ")
    num = int(num)
    if num < 100:
        print("Try higher")
    elif num > 100:
        print("Try lower")
    else:
        print("Hold on right there!")
        break   
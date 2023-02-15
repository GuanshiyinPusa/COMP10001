x = "not a number"
while type(x) != int:
    try:
        x = int(input("please enter a number: "))
    except ValueError:
        print("Oops! Try again!\n")
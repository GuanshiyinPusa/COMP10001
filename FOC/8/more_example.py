while True:
    try:
        x = input("Please enter an integer: ")
        print(1/int(x))
    except ValueError:
        print("That is not an integer\n")
    except ZeroDivisionError:
        print("Cannot find the recipricol of 0\n")
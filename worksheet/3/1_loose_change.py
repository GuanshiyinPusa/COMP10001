try:
    raw_cost = float(input("How much does it cost? "))
    cost = 100 * raw_cost
    cost = round(cost, -1)
    if cost % 5 == 0:
        print("The price didn\'t change or was rounded down! Pay cash!")
    else:
        print("The price was rounded up! Pay card.")
except ValueError:
    print("Invalid input. Please enter a number.")
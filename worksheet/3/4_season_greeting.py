num = input('Enter the month (1-12): ')
try:
    num = int(num)
    if num in (1, 2, 12):
        print("It's summer. Have fun in the sun!")
    elif 3 <= num <= 5:
        print("It's autumn. Enjoy the beautiful sunsets!")
    elif 6 <= num <= 8:
        print("It's winter. Go skiing!")
    elif 9 <= num <= 11:
        print("It's spring. Check out the spring racing carnival!")
except ValueError:
    print("Invalid input. Please enter any number between 1 and 12.")

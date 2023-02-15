hei = input('Enter height: ')

if hei.isdigit():
    num = int(hei)
    temp = 1
    while temp <= num:
        print('*' * temp)
        temp += 1
else:
    print("Invalid input")

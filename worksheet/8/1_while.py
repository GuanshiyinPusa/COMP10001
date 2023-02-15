num = input('Enter the number for \'num\': ')
N = input('Enter the number for \'N\': ')
if not (num.isdigit() and N.isdigit()):
    print('Invalid input')
elif int(num) >= 1 and int(N) >= 1:
    for temp in range(1, int(N) + 1):
        res = temp ** int(num) 
        print(f'{temp} ** {num} = {res}')
else:
    print('Invalid input')

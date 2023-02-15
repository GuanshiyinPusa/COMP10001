hei = input('Enter triangle height: ')
num = int(hei)
temp1 = 0
temp2 = num

while temp1 <= num // 2:
    print('*' * temp2 + ' ' * 2 * temp1 + '*' * temp2)
    temp1 += 1
    temp2 -= 1

temp3 = num // 2 + 1 if num % 2 == 0 else num // 2 + 2
temp4 = num // 2 - 1 if num % 2 == 0 else num // 2

while temp3 <= num :
    print('*' * temp3 + ' '  * 2 * temp4 + '*' * temp3)
    temp3 += 1
    temp4 -= 1

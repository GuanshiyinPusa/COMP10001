Q = input('Question: ')
num = float(Q[13:15])
price = float(Q[-6:-1])
each = format(price/num,".2f")
print('$'+str(each))
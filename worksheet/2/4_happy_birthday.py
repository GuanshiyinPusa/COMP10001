days = input('How many days have you lived? ')
ndays = int(days)
yrs = ndays // 365
print('You are ' + str(yrs) + ' years young!')
left = (yrs+1)*365 - ndays
print('You have ' + str(int(left)) + ' days until you next get to boogie down.')
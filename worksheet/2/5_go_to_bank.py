bemon = input('How much money would you like to invest, Mr Frodo? ')
damon = input('How many days would you like to invest this for? ')
be = float(bemon)
da = int(damon)
mon = float(da//31)
fimon = be*(1.0 + 0.045/12.0)**mon

print('After that time you will have: $'+ str(fimon))
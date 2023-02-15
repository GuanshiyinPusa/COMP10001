name = input('Enter your name, soldier: ')
if name == '':
    print('A luddite! GO AWAY AT ONCE!')
elif name in ['0', '1', '2']:
    print('HAHA! You may not pass!!')
else:
    print(f'Welcome to the camp, {name}, if that really is your name.')

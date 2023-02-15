lphrase = input('Enter a phrase: ')
phrase = lphrase.lower()
if len(phrase) > 0 and phrase[0] in 'aeiou':
    print('an ' + lphrase)
else:
    print('a ' + lphrase)

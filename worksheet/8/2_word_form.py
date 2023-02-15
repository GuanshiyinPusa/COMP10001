words = input('Enter the list of words: ') 
suffix = input('Enter the common suffix: ')
for ele in words.split():
    print(ele + suffix)

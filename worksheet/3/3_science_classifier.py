word = input('Hit me: ' )
if word[-5:] == 'omics':
    print('Life science hippy!')
elif word[:4] == 'comp' or word[:4] == 'info':
    print('Computing ftw!')
elif word[-1] == 'y':
    print('Au naturel!')
else:
    print('Too new to keep up!')

# word = input('Hit me: ')
# if word.endswith('omics'):
#     print('Life science hippy!')
# elif word.startswith(('comp', 'info')):
#     print('Computing ftw!')
# elif word.endswith('y'):
#     print('Au naturel!')
# else:
#     print('Too new to keep up!')

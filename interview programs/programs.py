# how to find if substring is available in main string
MainString = 'Welcome to python programming'

if MainString.find(input('Enter Substring : ')) == -1:
    print('Substring is Not Available')
else:
    print('Substring is Available')

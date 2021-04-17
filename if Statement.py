x = int(input("Please neter an integer"))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

#for statement
#measure some strings
words = ['cat', 'windows', 'defenestrate']
for w in words:
    print(w, len(w))


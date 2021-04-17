'"Isn\'t," they said.'
print('"Isn\'t," they said')

s = 'First Line. \nSecond line.' #\n means newline
s # without print(), \n is include in the output
'First line.\nSecond line.'
print(s) #With print(), \n produces a new line
print('c:some\name') #here \n newline!
print(r'c:\some\names') #the r before the quates
print("""\
Usage: thingy [OPTIONS]
    - h                         Display this usage message
    - H hostname                Host name to connect to
""")
print(3 * 'Afr'+'ica') # concatenate two literals by use of + with the literals enclose in ''



Prefix = 'Afri'
print(2 * Prefix + 'ica') # It is possible to concatenate a literal and a varriable by enclosing a varriable in side '' then an operator.

word = 'Python'
print(word[0]) #python counts character from 0,1,2,3......  (Zero is included)
print(word[5]) # n is the character at the 5th place in the word Pyhton
print(word[-1]) #Last characeter
print(word[-2]) #Second last character
print(word[0:2]) #Character from position 0 to 2 (Included)
print(word[:2] + word[2:]) #characters for the begining to position 2 and from end to position -2





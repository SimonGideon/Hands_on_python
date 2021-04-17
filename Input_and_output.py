# Fancier_output_formatting
year = 2016;
event = 'Referendum'
print(f'Results of the {year} {event}')

print('\n')

yes_votes = 42_572_654;
no_votes = 43_132_495
percentage = yes_votes / (yes_votes)
print('{:-9} YES votes {:2.2%}'.format(yes_votes, percentage))

print('\n')

s = 'Hello, world'
print(str(s))
print(repr(s))
print(str(1 / 7))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ',and y is ' + repr(y) + '...'
print(s)

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
# The argument to repr() may be any python object:
print(repr((x, y, ('spam', 'eggs'))))
print('\n')

# Formatted_string_literals
import math

print(f'The value of pi is approximately {math.pi:.3f}.')

print('\n')
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10}==> {phone:10d}')  # making column line up
print('\n')
animals = 'eels'
print(f'My hovercraft is full of {animals}.')

print(f'My hovercraft is full of {animals !r}.')  # modifier convert the value_before it is formatted.
print('\n')

# The_string_format() Method
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))  # key arguments used in str.format() method values referred to using
# argument name.
print('This {food} is {adjectives}.'.format(
    food='spam', adjectives='absolutely horrible'))  # Both positional & keyword arguments can arbitrarily combined:
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='George'))
# Formatting of strings by name instead of position.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}); '
      'Dcab: {Dcab:d}'.format(**table))  # Passing key word argument by ** notation.

print('\n')
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

print('\n')

# Manual Sting Formatting
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end='')
    print(repr(x * x * x).rjust(4))
print('\n')
print('12'.zfill(5))  # pads numeric string to the with 0's
print('-3.14'.zfill(7))

print('\n')

# Old_string_formatting
import math

print('The value of pi is approximately %5.3f.' % math.pi)

print('\n')

# Reading_and_writing Files
f = open('workfile', 'w')
with open('workfile') as  f:
    read_data = f.read()
print(f.closed)

print('\n')

# Method_of_file_objects

f = open('workfile', 'rb+')
print(f.write(b'0123456789abcdef'))
print(f.seek(5)) # go to the 6th byte in the file
print(f.read(1))
print(f.seek(-3, 2)) # Go to the 3rd byte before the end
print(f.read(1))

f.read()
'This is the entire file.\n'
f.read()

f.readline()
'This is thefirst line of the file.\n'
f.readline()
'second line of the file.\n'
f.readline()

for line in f:
    print(line, end='')

print('\n')
# Saving_structured_data_with_json
import json
print(json.dumps([1, 'simple', 'list']))







fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'orange']
x = fruits.count('orange')
print(x)
print(fruits.count('tangerines'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))  # Find next banana starting at position 4
fruits.reverse()
print(fruits)
fruits.append('grapes')
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()
print(fruits)

print("\n")
print("\n")
print("\n")

# Using List as Stacks
stack = [3, 4, 5]
stack.append(6)
print(stack)
stack.append(8)
print(stack)
stack.pop()
print(stack)

print("\n")
print("\n")
from collections import deque

queue = deque(['Eric', 'John', 'Michael'])
queue.append("Graham")
queue.append('Terry')
print(queue)
queue.popleft()
queue.popleft()
print(queue)  # First in first out
print("\n")
print("\n")
# List Comprehension
squares = []
for x in range(10):
    squares.append(x ** 2)
    print(squares)
    squares = list(map(lambda x: x ** 2, range(10)))
    print(squares)
    squares = [x ** 2 for x in range(10)]
    print(squares)

print("\n")

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)

print("\n")

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print([x * 2 for x in vec])

# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])

# apply a function to all elements
print([abs(x) for x in vec])

# call amethon on each element
freshfruit = [' banana', ' loganberry ', 'passion fruit ']
print([weapon.strip() for weapon in freshfruit])

# create a list of 2-tuples like (number, squre)
print([(x, x ** 2) for x in range(6)])  # the tuples must be parenthesized otherwise an error is raised.
# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 2], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])
# list comprehensions can contain complex expressions and nested functions
from math import pi

print([str(round(pi, i)) for i in range(1, 6)])

print("\n")
# Nested List Comprehension
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])  # Arrange the matrix into rows

transposed = []
for i in range(4):
    transposed.append(
        [row[i] for row in matrix])  # Here the nested list loopis evaluated in the context of the for that follows it

print(list(zip(*matrix)))  # Also gives the same results

print("\n")
# the_del_statement
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]  # Del function removes the value at the stated position
print(a)

print("\n")

# Tuple_and_sequences
t = 12345, 54321, 'hello!'
print(t[0])
u = t, (1, 2, 3, 4, 5)
print(u)
empty = ()
singleton = 'hello',  # ,-- note trailings comma
len(empty)
print(len(singleton))
print(singleton)

print("\n")

# sets
basket = {'apples', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # Duplictaes in the list has been removed; set don't support duplicate
print('orange' in basket)  # first member testing
print('crabgrass' in basket)

# Demonstrate_set_operations on unique_letters_from_two_words
a = set('abracadabra')
b = set('alacazam')
print(a)  # Repeated letters are omitted
print(a - b)  # letters in a but not in b

print(a | b)  # letters in a or b

print(a & b)  # letter in both a and b

print(a ^ b)  # letters in a or b but not in both

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

print("\n")

# dictionaries
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
# Dict() function builds dictionaries direct from sequences.

print("\n")

# looping_techniques
knights = {'galahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)  # Positioning index and corresponding value

questions = ['name', 'quest', 'favorite color']
answer = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answer):
    print('what is is your {0}? It is {1}.'.format(q, a))
# Loop over two or more sequences at the same time, entries can be paired with zip()

for i in reversed(range(1, 10, 2)):
    print(i)  # Looping over a sequence in reverse

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)  # Loop over sequence in sorted order

print("\n")

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)

print("\n")




from idlelib.idle_test.test_browser import module
from inspect import Traceback
from subprocess import call


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonolocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)


# class_objects
class MyClass:
    """A simple example class"""
    i = 12345


def f(self):
    return 'hello world'


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print((x.r, x.i))

print("\n")

# Instance_objects
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

print("\n")


# class_instance_variable
class Dog:
    kind = 'canine'  # class variable shared by all instances

    def __int__(self, name):
        self.name  # instances variable unique to each instance


d = Dog('Fido')
e = Dog('Bosco')
d.kind  # shared by all dogs
'canine'
e.kind  # shared by all dogs
'canine'
d.name  # unique to d
'Fido'
e.name  # unique to e
'Bosco'


class Dog:
    tricks = []  # mistake use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

    d = Dog('Fido')
    e = Dog('Bosco')
    d.add_trick('roll over')
    e.add_trick('play dead')
    d.tricks  # shared by all dogs


['roll over']
e.tricks
['play dead']
print("\n")


# Random_remark
# functions defined outside the class
def f1(self, x, y):
    return min(x, x + y)


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


class Bag:
    def __init__(self):
        self.data = []

    def __add__(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)


# Private_varriables
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in itterable:
            self.items_list.append(items)

    __update = update  # private copy of the original update() method


class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provides new signatures for update()
        # but does not break ___init___()
        for item in zip(keys, values):
            self.items_list.append(item)
print("\n")
# Odds_and_ends
class Employee:
    pass
john = Employee()  #creates an empty employee record

#Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

print("\n")
# iterators
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
s = 'abc'
it = iter(s)
it


next(it)
'a'
next(it)
'b'
next(it)
'c'
next(it)
Traceback (most recent call last):
    File "<stidin>", line 1, in <module>
    next(it)
StopIteration


class Reverse:
    """Iterator for looping over asequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        return self
    def __next__ (self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    rev = Reverse('spam')
    for(rev)
        for char in rev:
    print(char)

# Generators
def reverse(data):
    for index in range(len(data))-1, -1, -1):
        yield data[index]
    for char in reverse('golf'):
        print(char)




# Generator_expression
sum(i*i for i in range(10))    # sum of squares
print(sum)

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))    # dot product
print(sum)

from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
unique_words = set(word for line in page for word in line.split())
valedictorian = ma((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i  in range(len(data)-1, -1, -1))




print("\n")



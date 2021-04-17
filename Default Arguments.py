def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
    if ok in ('n', 'no', 'nop', 'nope'):
        return False
    retries = retries - 1
    if retries < 0:
        raise ValueError('invalid user response')
    print(reminder)


i = 5


def f(arg=1):
    print(arg)


i = 6
f()


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


# KEYWORD ARGUMENTS
def parrot(voltage, state='a stiff', action='voom', type='Norweigian Blue'):
    print("--This parrot would'nt", action, end='')
    print("if you put", voltage, "vols through it,")
    print("--Lovely plumage, the", type)
    print("--It's", state, "!")


def cheeseshop(kind, *arguments, **keywords):
    print("--Do you have any", kind, "?")
    print("--I'am sorry we're all out of", kind)
    for arg in arguments:
        print(arg)
        print("-" * 50)
        for kw in keywords:
            print(kw, ":", keywords[kw])


cheeseshop("Vegetables", "It's very runny, Sir.",
           "It's really very, very runny, sir.",
           shopkeeper="Simon G.",
           client="John MArk",
           sketch="Cheese shop sketch")
print(

)


# Arbitirary Argument List
def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "Jupiter", "Venus"))

print(

)


# Unpacking Argument Lists
def parrot(voltage, state='a stiff', action='voom'):
    print('--' * 10, "This parrot wouldn't", action, end='')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin", "action": "VOOM"}
parrot(**d)

"""This 
is 
a multiline

comment
"""
print("\n")
# Lambda Expressions.
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
print(f(0))
print(f(1))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[0]) #when one changes the value ofpair in the bracket for 0 to 1 this is from ascending to descending
print(pairs)

print('\n')
print('\n')
print('\n')
#Document Strings
def my_function():
    """Do nothing, but document it

    No really, it doesn't do anything
    """
    pass
print(my_function.__doc__)

print('\n')

#Fuction Anotation
def f(harm: str, eggs: str = 'eggs') -> str:
    print("Annotation:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + 'and' + eggs
f('spam')




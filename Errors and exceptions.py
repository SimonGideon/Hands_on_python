while True:
    try:
        x = int(input("Please enter a number:"))
        break
    except ValueError:
        print("Oops! That was no valid number. Try agian", ('....' * 10))
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
import sys
try:
    f = open('Numbers.py')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error: ",sys.exc_info()[0])
    raise
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst)) #the exception instance
    print(inst.args) # arguments stored in .args
    print(inst) # __str__ allows args to be printed directly
                # but may be overridden in exception subclasses
    x, y = inst.args # unpack args
    print('x =', x)
    print('y =', y)
def this_falls():
    x = 1/0

try:
    this_falls()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)




# User-defined_exceptions
class Error(Exception):
    """Base class for exceptions in this module."""
    pass
class InputError(Error):
    """Exception raised for errors in the input

    Attributes:
        expression -- input expression in which the error occured message -- explanation of error
        """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not allowed.
    """
def __init__(self, previous, next, message):
    self.previous = previous
    self.next = next
    self.message = message

# Defining_clean-up_actions
try:
    raise keyboardInterrupt
finally:
    print('Goodbye, world!')
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
divide(2, 1)
divide(2,0)





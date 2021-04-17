# Fibonacci numbers modules
def fib(n):  # write Fibonacci series up to  n
    a, b = 0, 1
    while a < n:
        print(a, end='')
        a, b = b, a + b
        print()


def fib2(n):  # Write fibonacci series upto n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

    import fibo
    fibo.fib(1000)
    fibo.fib2(100)
    fib = fibo.fib
fib(500)

# Executing_modules_as_scripts
if __name__ == "__main__":
    import sys

    fib(int(sys.argv[1]))

# Standard_modules
import sys

sys.ps1
'>>>'
sys.ps2
'...'
sys.ps1 = 'c>'
c > print('Yuck!')
import sys

sys.path.append('/ufs/guido/ib/python')

# The_dir()_function
import fibo, sys

dir(fibo)
dir(sys)

a = [1, 2, 3, 4, 5]
import fibo

fib = fibo.fib
dir()

# Packages
echo.echofilter(input, output, delay=0.7, atten=4)

# Import_*From_a_Package
import sound.effects.echo
import sound.effects.surround
from sound.effect import *

# Intra-package References
from . import echo
from .. import formats
from ..filters import equilizer





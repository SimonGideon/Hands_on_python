#the sum of two elements defines the next


a, b = 0, 1

while a < 10:
    print(a)
    a, b = b, a+b
i = 256*256
print('The value of i is',i)


a, b = 1, 0
while a < 1000:
    print(a, end=',')
    a+=1

#@ Range
for i in range(5):
    print(i)
print(range(10))

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals' 'x', '*',n // x)
            break
        else:
            print(n, 'is a prime number')



for num in range(2,10):
    if num % 2 == 0:
        print("Found a number", num)
        continue
    print("Found an odd number", num)
    break

    break
def fib(n):
    """Print a Fibonacci series upto n."""
    a, b = 0, 1
    while a < n:
        print(a, end='')
        a, b = b, a + b
    print( )

# Now call the function defined above
fib(2000)

fib
f = fib
f(100)


def fib2(n): #returns Fibonacci Serires upto n
    """Returna list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
f100





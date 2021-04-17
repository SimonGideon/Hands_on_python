x = int(input("Please enter an interger: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
# elif is used to avoid repetation of if statement

# for_statement
words = ['cat', 'window', 'differentiation']
for e in words:
    print(e, len(e)) # the function 'len' is for counting.
for e in words[:]:
    if len(e) >6:
        words.insert(0, e) # insert the word with characters > 6 at position 0.
print(words)

# The_the_range_function
for i in range(1, 50, 9):
    print(i)

a = ['We', 'will', 'go', 'today']
for i in range(len(a)):
    print(i, a[i])
print(list(range(10))) # output , will be "range(0,10)" unless the list function is included.

# Break_and_continue_statements_else_clause_on_loop
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')
for num in range(2, 20):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num, "I think is an odd")
    

# Defaulf_argument_vallue
def ask_ok(promt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return False
        if retries < 0:
            raise ValueError('Invalid user response')
        print(reminder)
        


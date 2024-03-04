# f = open('simon.csv', 'w')
# f.write("Python is awesome")
# f.close()
# print(open('simon.csv', 'r').read())
# modes
# x- creates
# w - write
# r - read
# a - append
prime_numbers = []
for i in range(1, 11):
    if i > 1:
        for numb in range(2, i):
            if (i % numb) == 0:
                break
        else:
            prime_numbers.append(i)
with open("results.txt", "w") as file:
    file.write(str(prime_numbers) + "\n")
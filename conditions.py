# name = input("Enter your name: ")

# nm = len(name)
# if nm > 0:
#     print("Good trails")
# elif nm > 3:
#     print("Better")
# elif nm > 5:
#     print("Best")

# relational operators
# <, >, >=, <=, ==, !=
# logical operators
# and(&&), or(||), not(!)


# age = int(input("Enter your age: "))

# if age < 18:
#     print("You are not eligible to vote")
# else:
#     print("You are eligible to vote")

# counter = 0
# while counter < 10:
#     print(" The counter is: ", counter)
#     counter += 1
# import random

# n = random.randint(1, 10)
# guess = 0

# while guess != n:
#     guess = int(input("Enter your guess: "))
#     if guess > n:
#         print("Too high")
#     elif guess < n:
#         print("Too low")
#     else:
#         print("You got it!")
#         break

# working with lissts
# names = ["John", "Paul", "George", "Ringo"]
# print(names[0])
# print(len(names))
# print(names[2:4])
# names.append("Pete")
# names.insert(2, "Stu")
# names.sort()
# print(names)
# names.reverse()
# for name in names:
#     print(name)

# Dictionary
# dict = {"name": "John", "age": 30, "city": "New York"}
# dict["email"] = "testemail@gmail.com"
# print(dict.items())

# for key, value in dict.items():
#     print(key, value)

# functions
def greet(name):
    print("Hello, " + name + ". Good morning!")


greet("John")

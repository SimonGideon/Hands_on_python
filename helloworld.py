import json
filename = 'userName.json'
name = ''

# check for a history file
try:
    with open(filename, 'r') as r:
        # load the user name from the history file
        name = json.load(r)
except IOError:
    print("First-time login")
# if the suer was found in the history file, welcome tem back
if name != "":
    print("Welcome Back " + name + "!")
else:
    name = input("Hello! what's your name? ")
    print("Welcome, " + name + "!")
try:
    with open(filename, 'w') as f:
        json.dump(name, f)
except IOError:
    print("There was a problem writing to the history file.")

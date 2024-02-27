number = int(input("Enter a number divide by 5: "))
def divide_five_by(num):
    try:
        ans=5/num

    except ZeroDivisionError:
        print("Cannot divide by zero")
    print(ans)

divide_five_by(number)
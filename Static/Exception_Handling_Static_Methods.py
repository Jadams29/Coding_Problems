import random

try:
    aList = [1,2,3]
    print(aList[3])
except (IndexError,NameError):
    print("Sorry that index doesnt exist")
except:
    print("An unknown error occurred")


class DogNameError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    dogName = input("What is your dogs name : ")
    if any(char.isdigit() for char in dogName):
        raise DogNameError
except DogNameError:
    print("Your dogs name can't contain a number")


num1, num2 = input("Enter two values to divide ").split()

try:
    quotient = int(num1) / int(num2)
    print("{} / {} = {}".format(num1, num2, quotient))

except ZeroDivisionError:
    print("You can't divide by zero")
else:
    print("You didn't raise an exception")

finally:
    print("I execute no matter what")
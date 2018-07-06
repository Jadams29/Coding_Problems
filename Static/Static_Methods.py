# Static methods allows access with out the need to initialize an object
import Sum

print("Sum : {}".format(Sum.getSum(1, 2, 3, 4, 5)))

class Sum:
    @staticmethod
    def getSum(*args):
        sum = 0
        for i in args:
            sum += i
        return sum

class Dog:
    # num_of_dogs is a static variable so it will change for all created objects as it changes
    num_of_dogs = 0

    def __init__(self, name = 'Unknown'):
        self.name = name
        Dog.num_of_dogs += 1

    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))


def main():
     print("Sum : {}".format(Sum.getSum(1,2,3,4,5)))
     spot = Dog('Spot')
     spot.getNumOfDogs()
     steve = Dog('Steve')
     spot.getNumOfDogs()
     steve.getNumOfDogs()

main()
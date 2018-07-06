# Dynamic Function
def get_func_mult_by_num(num):

    def mult_by(value):
        return num * value

    return mult_by

generated_func = get_func_mult_by_num(5)

print("5 * 10 = ", generated_func(10))

def testing_function(number1):
    def inner_func(number2):
        return number1, number2
    return inner_func

tester = testing_function(32)

print("This should print out two numbers: ", tester(64))

def mult_by_2(num):
    return num * 2
times_two = mult_by_2


# List of functions listOfFuncs[0] would call times_two
listOfFuncs = [times_two, generated_func]

print("5 * 9 =", listOfFuncs[1](9))

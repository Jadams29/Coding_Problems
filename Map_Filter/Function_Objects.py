def mult_by_2(num):
    return num * 2

times_two = mult_by_2

print("4 * 2 = ", times_two(4))

def do_math(function, num):
    return function(num)

# Passing a function into another function
print("8 * 2 =", do_math(mult_by_2,8))
# Prime number generator

def isPrime(num):
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

def gen_Primes(max_number):
    for num1 in range(2, max_number):
        if isPrime(num1):
            yield num1

prime = gen_Primes(50)

print("Prime :", next(prime))
print("Prime :", next(prime))
print("Prime :", next(prime))
print("Prime :", next(prime))
print("Prime :", next(prime))
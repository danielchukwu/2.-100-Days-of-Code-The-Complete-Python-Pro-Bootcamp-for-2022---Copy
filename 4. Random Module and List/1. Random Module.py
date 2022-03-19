# Python - 3.10
# Topic - Random Module
# program - The random module returns a pseoudo random number. which is very important in programming
#           1. random.randint(a, b) => takes 2 arguments (a and b) and returns integer number including a and b
#           2. random.random() => takes no argumemt and returns float number inbetween 0 and 1 but excluding 0 and 1


# learning - done
import random

# integers: use random.randint(a, b)
print("\nRandom.randint(a,b) - integers")
random.randint(1, 10)
random.randint(0, 50)

print(random.randint(1, 10))
print(random.randint(0, 50))


# floating-point: use random.random()   note: takes no arguments
print("\nRandom.random() - floats")
random.random()

print(random.random())

#     - to get floating-point number between numbers other than just 0 and 1 e.g 0 and 5
#        - multiply random.random() by 5
print("\n - between 0 and 5")
print(random.random() * 5)


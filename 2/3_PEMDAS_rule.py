# Python - 3.10
# Topic - PEMDAS
# program - Order of Arithmethical Operations in Python


# Arithmetical Operations
4 + 4
7 - 4
3 * 2
6 / 3   # result = 2.0; note: division in python always returns a floating point data type
2 ** 3

# PEMDAS - Execution from left to right
# Parentheses - ()
# Exponents - **
# Multiplication - *
# Division - /
# Addition - +
# Subtraction - -


# Quiz: what will be the result of the below arithmetical operation
3 * 3 + 3 / 3 - 3

# step: 1
(3 * 3) + 3 / 3 - 3
(9) + 3 / 3 - 3

# step: 2
((3 * 3) + (3 / 3)) - 3
((9) + (1.0)) - 3

# step: 3
(((3 * 3) + (3 / 3)) - 3)
((10.0) - 3)

# step: 4
7

# Prove
print(3 * 3 + 3 / 3 - 3)



# ...
# Quit: how do we alter the arithmetical operation to get the result of 3
3 * 3 + 3 / 3 - 3

# Ans: by adding parenthesis to 3 + 3
3 * (3 + 3) / 3 - 3

# prove
print(3 * (3 + 3) / 3 - 3)


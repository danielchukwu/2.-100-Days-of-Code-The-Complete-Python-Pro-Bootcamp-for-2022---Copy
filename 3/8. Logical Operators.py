# Python - 3.10
# Topic - logical operators
# program - and, or, not



# learning - done

# and operator(both conditions have to be true)
print("\nAND operators")
10 > 5 and 10 < 15     # => True
10 > 4 and 10 < 8      # => False

print(10 > 5 and 10 < 15 )
print(10 > 4 and 10 < 8 )

# or operator(true as long as one condition is true)
print("\nOR operators")
10 > 5 or 10 < 15     # => True
10 > 4 or 10 < 8      # => True

print(10 > 5 or 10 < 15 )
print(10 > 4 or 10 < 8 )

# not operator(changes the evaluation of a  conditional statement to the opposite)
print("\nNOT operators")
not(10 > 5 and 10 < 15)     # => False
not(10 > 4 and 10 < 8)      # => True

print(not(10 > 5 and 10 < 15))
print(not(10 > 4 and 10 < 8))
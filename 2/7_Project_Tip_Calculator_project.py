# Python - 3.10
# Topic - Tip Calculator Project
# program - create a program that adds a tip percentage to the bill and splits the bill 
#           between some amount of people

# Result should be in this format:
# Welcome to the tip calculator.
# What was the total bill? $124.56
# What percentage tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7
# Each person should pay: $19.93


# program - undone✅

# intro
print("\nTIP CALCULATOR PROJECT")

# welcome to the program
print("welcome to the tip calculator.")

# input: enter the total bill
total_bill = input("What was the total bill? $")

# input: enter the tip
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

# input: enter amount of people to split the bill amongst
split_bill = input("How many people to split the bill? ")

# calculate: get tip percentage and add to bill
tip = (int(tip_percentage) / 100) * float(total_bill)
total_bill = float(total_bill) + tip

# calculate: split the bill
bill = total_bill / int(split_bill)
# final_bill = round(bill, 2)              # we only want bill in 2-decimal places
# OR
final_bill = "{:.2f}".format(bill)

# output: in f-String
print(f"Each person should pay: ${final_bill}")

# Spin-off .....
# decimal places:
# print("{:.3f}".format(2))                 # => 2.000
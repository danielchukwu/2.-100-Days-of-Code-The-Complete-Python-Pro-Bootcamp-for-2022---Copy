# Python - 3.10
# Topic - BMI calculator project
# program - write a program that calculates the Body Mass Index (BMI) from a user's weight and height.


# program - done


# input for user weight and height
weight = input("Enter weight(kg): ")
height = input("Enter height(m): ")

# calculate the BMI
body_mass_index = int(float(weight) / float(height)**2)

# output:
print(body_mass_index)
# Python - 3.10
# Topic - BMI 2.0 calculator
# program - write a program that interprets the Body Mass Index (BMI) based on a user's weight and height
# it should tell them the interpretation of their BMI based on the BMI value.
#    Under 18.5 are underweight
#    Over 18.5 but below 25 they have a normal weight
#    Over 25 but below 30 they are overweight
#    Over 30 but below 35 they are obese
#    Above 35 they are clinically obese.


# program - done✅

# input for user weight and height
weight = input("Enter weight(kg): ")
height = input("Enter height(m): ")

# calculate the BMI
bmi = int(float(weight) / float(height)**2)
print(bmi)

# output: give an interpretation
if bmi <= 18.5:
   print(f"your bmi is {bmi}, you are underweight")
elif bmi > 18.5 and bmi <= 25:
   print(f"your bmi is {bmi}, you have a normal weight")
elif bmi > 25 and bmi <= 35:
   print(f"your bmi is {bmi}, you are obese")
elif bmi > 35:
   print(f"your bmi is {bmi}, you are clinically obese.")
else:
   print(f"your bmi is {bmi}, God is good!")

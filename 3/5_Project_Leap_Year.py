# Python - 3.10
# Topic - Leap Year project
# program - write a program that works out whether if a given year is a leap year. A normal year has 365 days, 
#           leap years have 366, with an extra day in February
# How to know if a year is a leap year
# 1. On every year that is evenly divisible by 4
#    2. except every year that is evenly divisible by 100
#      3. unless the year is also evenly divisible by 400


# program - 

# intro
print("\nLEAP YEAR PROGRAM")

# declared
leap_year = None

# input: recieve year input
year = int(input("Enter a year: "))


# process: calculate if input is a leap year
if (year % 4 == 0):
   # print(f"the year is evenly divisible by 4 in {year / 4}")
   leap_year = True

   if (year % 100 == 0):           
      if (year % 400 == 0):
         leap_year = True
      else:
         leap_year = False
      
   else:
      leap_year = True
   
else:
   leap_year = False


# output: display
if leap_year == True:
   print(f"so the year {year} is a leap year")
else:
   print(f"so the year{year}, is not a leap year")
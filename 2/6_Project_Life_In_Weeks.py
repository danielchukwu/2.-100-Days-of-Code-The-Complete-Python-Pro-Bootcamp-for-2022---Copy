# Python - 3.10
# Topic - Life in weeks project
# program - create a program using maths and f-Strings that tells us how many days, weeks, months we have 
#           left if we live until 90 years old.
# result should be in this format:
# - you have x days, y weeks, and z months left


# program - done✅

# intro
print("\nLIFE IN WEEKS PROGRAM")

# constant
weeks_in_a_year = round(52.1429)
months_in_a_year = 12
days_in_a_year = 365
total_years_to_live = 90

# input: enter how old you are
user_age = input("How old are you?: ")

# calculate years left(90years - age), 
years_left = total_years_to_live - int(user_age)

# calculate weeks_left = years * weeks/yr
days_left = int(years_left  * days_in_a_year)
weeks_left = int(years_left * weeks_in_a_year)
months_left = int(years_left * months_in_a_year)

# output: in f-String
print(f"you have {days_left} days, {weeks_left} weeks, and {months_left} months left")
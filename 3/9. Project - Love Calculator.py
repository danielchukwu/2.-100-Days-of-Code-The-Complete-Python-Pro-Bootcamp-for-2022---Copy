# Python - 3.10
# Topic - Love Calculator program
# program - You are going to write a program that tests the compatibility between two people. We're going 
#           to use the super scientific method recommended by BuzzFeed.

# To work out the love score between two people:
# - Take both people's names and check for the number of times the letters in the word TRUE occurs.
# - Then check for the number of times the letters in the word LOVE occurs.
# - Thn combine these numbers to make a 2 digit number

# hint:
# - you will need two functions
#   1. lower()
#   2. count()

# For love scores less than 10 or greater than 90, the message should be:
#  "Your score is x, you go together like coke and mentos."
# For love scores between 40 and 50, the message should be:
#  "Your score is y, you are alright together."
# Otherwise, the message will just be their score. e.g.:
#  "Your score is z."


# program - undone


# intro
print("LOVE CALCULATOR PROGRAM!")
print("\nWelcome to the Love Calculator")

# input: recieve input for 1st person and 2nd person
first_person = input("What is your name? ").lower()
second_person = input("What is their name? ").lower()

name = first_person + second_person  # join names together

# process: 
# 1st: true_total = check how many times TRUE appears in both 1st and 2nd persons names
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")

true_total = t + r + u + e
print(f"true_total: {true_total}")

# 2nd: love_total = check how many times LOVE appears in both 1st and 2nd persons names
l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

love_total = l + o + v + e
print(f"love_total: {love_total}")

# 3rd: love_score = true_total + love_total
love_score = int( str(true_total) + str(love_total) )

# output:
if (love_score < 10) or (love_score > 90):
   print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
   print(f"Your score is {love_score}, you are alright together.")
else:
   print(f"Your score is {love_score}.")

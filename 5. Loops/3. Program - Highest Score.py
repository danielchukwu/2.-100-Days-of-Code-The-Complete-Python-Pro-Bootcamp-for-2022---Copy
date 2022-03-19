# Python - 3.10
# Topic - Highest Score Program
# program - write a program that calculates the highest score from a List of scores.
#           e.g student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Hint: max() => this returns the maximum number in a list or argument containing the maximum number
#   another that won't be used is the
#       min() => this returns the minimum number in a list or argument containing the minimum number


# program - done✅

# intro:
print("\nHIGHEST SCORE - PROGRAM")

# input: recieve input
list_of_scores = input('Enter scores seperated with comma. : ').split(', ')

# needed: variable to store current highest score in list_of_scores
highest_score = 0

# process: use for loop
for score in list_of_scores:
   score = int(score)
   if score > highest_score:
      highest_score = score

# output: 
print(highest_score)





# Easier method 💖
print("Easier method")
highest_score = max( [int(score) for score in list_of_scores] )
print(highest_score)
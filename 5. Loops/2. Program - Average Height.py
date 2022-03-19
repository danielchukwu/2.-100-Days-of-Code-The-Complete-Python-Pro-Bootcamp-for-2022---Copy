# Python - 3.10
# Topic - Average Height Program
# program - write a program that calculates the average student height from a List of heights.
#           e.g student_heights = [180, 124, 165, 173, 189, 169, 146]
# Hint: sum() : finds the largest number in a list
#       len() : returns the total number of items in a list



# program - done✅

# intro
print("\nAverage Height Calculator - PROGRAM")

# input: recieve list of heights
list_of_heights = input("Enter a list of heights. each height seperated by a comma: ").split(', ')
print(list_of_heights)

# needed: variable to store height addition in loop
total_height = 0
length_of_list = 0

# process:
# intro:
print("Average Height - Program")

# 1st: loop through the list and add all the heights in the list
for height in list_of_heights:
   total_height += int(height)
   length_of_list += 1

# 2nd: Average = divide the summation of all the heights in the list by the length of the list
average = round( total_height / length_of_list )

# output:
print(f"Average height = {average}")



# Easier method 💖
print("\nEasier Method => Same Program")
total_height = sum( [int(x) for x in list_of_heights] )     # logic: one line for loop that converts all values in list from str => int
length_of_list = len(list_of_heights)

average = round( total_height/length_of_list )
print(average)
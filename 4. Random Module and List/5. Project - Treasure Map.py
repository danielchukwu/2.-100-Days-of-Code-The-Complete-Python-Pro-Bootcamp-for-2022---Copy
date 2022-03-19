# Python - 3.10
# Topic - Treasure Map program
# program - write a program which marks a spot with an X
# The map is made of 3 rows of blank Squares.
#      1     2     3
# 1 ['🔲','🔲', '🔲']
# 2 ['🔲','🔲', '🔲']
# 3 ['🔲','🔲', '🔲']
# your program should allow you to enter the position of the treasure using a two-digit system. The first digit is the horizontal column number and the second digit is the vertical row number. e.g
# coumn 2, row 3 would be entered as:
# => 23
# output:
# ['🔲','🔲', '🔲']
# ['🔲','🔲', '🔲']
# ['🔲','X', '🔲']



# program - done✅

# intro
print("\nTREASURE MAP - PROGRAM")

# create map
row_1 = ['🔲','🔲','🔲']
row_2 = ['🔲','🔲','🔲']
row_3 = ['🔲','🔲','🔲']

map = [row_1, row_2, row_3]

print(f"{row_1}\n{row_2}\n{row_3}")

# input: recieve position
position = input("where do you want to put the treasure? ")

# process:
# 1st: get column and row from position
row = int( position[0] )
col = int( position[1] )

# 2nd: switch the position value using col and row to "X"
map[row-1][col-1] = "X"

# output:
print(f"{row_1}\n{row_2}\n{row_3}")
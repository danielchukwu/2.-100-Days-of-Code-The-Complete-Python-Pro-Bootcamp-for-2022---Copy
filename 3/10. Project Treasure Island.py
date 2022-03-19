# Python - 3.10
# Topic - Treasure Island program
# program - create a program that leads you to the treasuce if you pick the right options

# How p
# Welcome to Treasure Island.
# Your mission is to find the treasure.
# You're at a cross road. Where do you want to go? Type "left" or "right"
# left => continue
# right => GAMEOVER

# You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.
# wait => continue
# swim => GAMEOVER

# You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?
# blue => GAMEOVER. you enter a room of beasts
# red => GAMEOVER. you enter a room full of zombie pirates
# yellow => continue. you find the treasure



# program - undone🔴 

# intro
print("TREASURE ISLAND PROGRAM!")
print("\nWelcome to Treasure Island.\nYour mission is to find the treasure.")

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Daniel]
*******************************************************************************''')

# process: choice 1, choice 2, choice 3 => Nested if statements that lead to the treasure
# choice 1
choice_1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()

if choice_1 == 'left':
   choice_2 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()

   if choice_2 == 'wait':
      choice_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()

      if choice_3 == 'yellow':
         print("you found the treasure🤘😛💪💪‼")
      elif choice_3 == 'blue':
         print("you enter a room of beasts")
      else:
         print("you enter a room full of zombie pirates")

   else:
      print("You drown while you were at it. GAMEOVER!")
      
else:
   print("you run into a 23 feet tall rattle snake. GAMEOVER!")



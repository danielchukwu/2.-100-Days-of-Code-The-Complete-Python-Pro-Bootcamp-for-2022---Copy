# Python - 3.10
# Topic - Rock Paper Scissors project
# program - write a program where we can play rock paper scissors with the computer

# 3 simple rules:
# Rock wins against scissors.
# Scissors wins against paper.
# Paper wins against rock.


# program - done✅🔴
import random
import time

# intro
print("\nROCK PAPER SCISSORS - PROGRAM")

# constant
rps = ['rock', 'paper', 'scissors']

won = False
lost = False

rock = """
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# print(f"{rock}\n{paper}\n{scissors}")

# helper funtions:
def printHand(hand):
   if hand == 0:
      print(rock)
   elif hand == 1:
      print(paper)
   elif hand == 2:
      print(scissors)

def checkForWinner(user, cpu):
   won = False
   lost = False

   if (user == 0) and (cpu == 1):  # rock and paper: lost = True
      lost = True
   elif (user == 0) and (cpu == 2):   # rock and scissors:  won = True
      won = True
   elif (user == 1) and (cpu == 0):   # paper and rock:  won = True
      won = True
   elif (user == 1) and (cpu == 2):   # paper and scissors:  lost = True
      lost = True
   elif (user == 2) and (cpu == 0):   # scissors and rock:  lost = True
      lost = True
   elif (user == 2) and (cpu == 1):   # scissors and paper:  won = True
      won = True
   else:
      print("tie!!!")
   
   return won, lost


# process: while there is no winner
while (won != True) and (lost != True):
   # 1st: input => user turn: enter Rock, Paper, Scissors
   user_pick = int( input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n") )
   printHand(user_pick)


   # 2nd: input => cpu turn: enter Rock, Paper, Scissors
   time.sleep(0.3)
   print("computer chose:")
   cpu_pick = random.randint(0, 2)
   printHand(cpu_pick)
   
   # 3rd: check if there is a winner
   won, lost = checkForWinner(user_pick, cpu_pick)


# output: 
if won:
   print("You won!")
else:
   print("You Lost!")

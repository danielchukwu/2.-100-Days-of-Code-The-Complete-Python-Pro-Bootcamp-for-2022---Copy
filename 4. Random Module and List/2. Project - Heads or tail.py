# Python - 3.10
# Topic - Heads or Tail program
# program - You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".


# program - done✅
import random

# intro
print("\nHEADS OR TAIL PROGRAM")

# process:
# 1st: coin toss => get random number between 0 and 1
coin_toss = random.randint(0, 1)

# 2nd: Check if its Heads(1) or Tail(0)
if coin_toss == 1:
   print("Heads")
else:
   print("Tail")


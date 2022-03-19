# Python - 3.10
# Project - Band Name Generator 
# program - 1. write a program that askes for the name of user's city they grew up in and pet's name 
#           2. then concatenate both to form a band name for the user
#           3. the program should look similar to the one we have below
# Expected Result:
# line 1: welcome to the Band Name Generator.
# line 2: What's name of the city you grew up in?
# line 3: Bristol
# line 4: What's your pet's name?
# line 5: Rabbit
# line 6: Your band name could be Bristol Rabit


# program - done
print("Welcome to the Band Name Generator.")

city = input("What's name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")

band_name = city + " " + pet_name

print("Your band name could be " + band_name)



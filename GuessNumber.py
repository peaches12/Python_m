# Guess a number from 1 to 10

import random # the computer will generate random number from 1 to 10

numPC = random.randint(1,10)
print("numPC: " + str(numPC))

print("Do you want to guess a number from 1 to 10?")
print("Enter Yes/No: ")

num = int(input("Enter a number from 1 to 10: "))
print("your number: " + str(num))

#create a function

if num < numPC:
    print("It is too low")
    print("Try again")
elif num > numPC:
    print("It is too high")
    print("Try again")
else:
    print("It is correct")

print("The end of the game")

    
          

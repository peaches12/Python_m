
import random
scorePlayer = int()
scoreComputer = int()
scoreTie = int()


playRounds = input("Enter how many times you want to play: ")
n = 1
if int(playRounds) <= 0:
    print("Wrong entry")
    print("Try again")
else:
    print()
    while n<=int(playRounds):
     print("Play " + str(n))
     choicePlayer = input("Choose (P)aper, (R)ock, (S)cissors : ")
     choiceComputer = random.choice("RPS")

     print("Player: " + choicePlayer + "   Computer: " + choiceComputer)
        
     if choicePlayer == "P" or choicePlayer == "p":
         if choiceComputer == "P":
             print("It is a tie")
             scoreTie = scoreTie + 1
          
         elif choiceComputer == "R":
             print("Player won")
             scorePlayer = scorePlayer + 1
         elif choiceComputer == "S":
             print ("Computer won")
             scoreComputer = scoreComputer  + 1
             
         else:
             print("Wrong entry")
             
     elif choicePlayer == "R" or choicePlayer == "r":
         if choiceComputer == "P":
             print("Computer won")
             scoreComputer = scoreComputer + 1
         elif choiceComputer == "R":
             print("It is a tie")
             scoreTie = scoreTie + 1
             
             
         elif choiceComputer == "S":
             print("Player won")
             scorePlayer = scorePlayer  +1
             
         else:
             print("Wront entry")
             
     elif choicePlayer == "S" or choicePlayer == "s":
         if choiceComputer == "P":
             print("Player won")
             scorePlayer = scorePlayer +1
             
         elif choiceComputer == "R":
             print("Computer won")
             scoreComputer = scoreComputer  + 1
             
         elif choiceComputer == "S":
             print( "It is a tie")
             scoreTie = scoreTie + 1
             
         else:
             print("Wrong entry")
     else:
         print("Wrong entry")

     print()
     
     n= n+1 

    print("******************************************************")
    print()

    print("Score: Player = " + str(scorePlayer) + "  Computer = " + str(scoreComputer))
    print("Tie = " + str(scoreTie))
    print()
    if scorePlayer > scoreComputer:
         print("Player won!")
    elif scorePlayer < scoreComputer:
         print("Computer won!")
    else:
         print("It is a tie")
    print()
    print("End of the game")




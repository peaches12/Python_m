# the program will calculate the number of characters in the string

print("Your string can only contain characters")
print()
choice = input("Do you want to start? yes/no: ")
print()


while choice.upper() == "YES":
    word = input("Enter a string: " )
    a=b=c=d=0
    for i in word:
                  if i.upper() == "A":
                      a = a+1
                  elif i.upper()== "B":
                      b=b+1
                  elif i.upper()== "C":
                      c=c+1
                  else:
                      
                      print("Your string must only contain characters.Try again")
    if choice.upper()== "YES" and(a>0,b>0,c>0):
             print()
             print("The frequency of characters: ")
             print("------------------------------")
             if a>0:
                 print("a/A = " + str(a))
                 if b>0:
                     print("b/B = " + str(b))
                     if c>0:
                         print("c/C = " + str(c))
else:
                 print()

choice= input("Do you want to continue? yes/no: ")
while choice.upper()== "YES":
     a=b=c=d=0
     word = input("Enter a string: " )
     end=str()
     for i in word:
                    if i.upper() == "A":
                          a = a+1
                    elif i.upper()== "B":
                          b=b+1
                    elif i.upper()== "C":
                          c=c+1
                    else:
                      print("Your string must only contain characters.Try again")
choice = input("Do you want to try again? yes/no: ")
if end != "The End" and(a>0,b>0,c>0):
             print()
             print("The frequency of characters: ")
             print("------------------------------")
             if a>0:
                 print("a/A = " + str(a))
                 if b>0:
                     print("b/B = " + str(b))
                     if c>0:
                         print("c/C = " + str(c))
             else:
                 print()


                      
print("END")             


#choice= input("Do you want to continue? yes/no: ")
   




    
        
    




                
            

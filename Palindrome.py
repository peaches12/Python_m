# the program will find out if a word is a palindrome ( the same reading forward and backward)

word = input("Enter a word here: ")

word2 = word[::-1] # to reverse the entered word
#choice = input("Do you want to play (Yes/No): ")

#while choice == "Yes":
if word.upper() == word2.upper():
     print("The word is a palindrome")

else:
     print("It is not a palidrome")
     
print("The end")

print()
print("**********************************************")

print("version 2")

Word = input("Enter you word here: ")
List= list(Word)
print(List)
ListRev =List[::-1]
print(ListRev)
print()
if List == ListRev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

print()






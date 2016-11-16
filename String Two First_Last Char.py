# the program will concatente the first two and the last two characters of
# the input string

word = input("Enter a string here: ")
word1=word[0:2]
word2=word[len(word)-2:]

print()
print("new string: " + (word1+word2))

print('-------------------------------')
choice= input("continue? yes/no: ")
while choice.upper() =="YES":
    word = input("Enter a string here: ")

    word1=word[0:2]
    word2=word[len(word)-2:]

    print()
    print("new string: " + (word1+word2))
no    print()
    print('-------------------------------')
    choice= input("continue? yes/no: ")

print('the end')




    

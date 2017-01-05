# the program will check if the list is empty

import random
#create a random list
a = int(input("Enter a number of items in the list: "))
myList = []
for r in range(a):
          myList.append(random.randrange(0,10,1))
print('your list is:' + str(myList))
          
print('Call the function "empty_list(myList)" ')


def empty_list(myList):
    
    if len(myList) == 0:
        print("the list is empty")
    else:
        print("the list is not empty")
    return;






          

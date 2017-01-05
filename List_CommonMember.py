#the program will create a function that takes two lists and returns True if
#there is at least one common item

import random

print('the range for the lists will be from 0 to 10')
list1 = []
list2 = []
num1 = int()
num2 = int()

num1 = int(input("enter a number of items in the first list: "))
num2 = int(input("enter a number of items in the second list: "))
           
for k in range(num1):
           list1.append(random.randrange(0,10,1))
print('list1: ' + str(list1))
#create a random list2
                             

for c in range(num2):
                list2.append(random.randrange(0,10,1))
print('list2: ' + str(list2))
                             
print()



print('call the function  "common_item(list1,list2)" ')
def common_item(list1,list2):
    
    a = 0
    n = 0
    while n < len(list1):
        m = 0
        while m < len(list2) and a == 0:
            if list1[n] == list2[m]:
                a = 1
                print("True")
                print("the lists have at least one common member")
            m = m + 1
        n  = n +1
    return;





        

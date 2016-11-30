#

import random
from operator import itemgetter

# random.seed()
low = 0
high = 10
myList = [(random.randint(0,10),) # each tuple contains one element
          for k in range(7)] # generate 7 tuples 
print('myList ' + str(myList))

myList2 =[
    (
    random.randint(0,10),
    random.randint(0,10) # each tuple contains 2 elements
    )
    for k in range(4) # generate 4 tuples
]

print('myList2 ' + str(myList2))


myList3 = [
    (random.randint(0,10),
     random.randint(0,10),
     random.randint(0,10) # each tuple contains 3 elements 
     )
    for k in range(5) # there will be 5 tuples 
    ]

print('myList3 ' + str(myList3))
print()


# to sort the tuples
print('sorted myList: ' + str(sorted(myList, key = itemgetter(0))) ) # itemgetter(0) for the element with the index = 0
print('sorted myList desc: ' + str(sorted(myList, key = itemgetter(0), reverse = True)))
print()

print('myList2 original: ' + str(myList2))
print('sorted myList2 by the second element of the tuples: ')
print( str(sorted(myList2 , key = itemgetter(1))) )
print('sorted myList2 desc by the second elemnet of the tuples: ')
print( str(sorted(myList2, key = itemgetter(1), reverse = True)) )
print()
print('myList3 original: ' + str(myList3))
print('myList3 sorted by the last element: ')
print(str(sorted(myList3, key = itemgetter(2))) )
print('myList3 sorted by the first and second element: ')
print(str(sorted(myList3, key = itemgetter(0,1))) )
print('myList3 sorted desc by the second element: ')
print(str(sorted(myList3, key = itemgetter(1), reverse = True)) ) 




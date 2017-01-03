#the program will convert the tuple into a string

myTuple = (1,2,3,4,5,0)




myList = []
myList = list(myTuple)

myString = str()

n = 0
while n < len(myList):
        myString1 = str(myList[n])
        myString = myString + myString1
        n = n + 1

print('tuple: ' + str(myTuple))

print('string: ' + myString)

#the program will add an item to the tuple

myTuple = (1,2,3,4,5,6)
print("the tuple " + str(myTuple))

item = input("enter an item you want to add to the tuple: ")
myList = []
newTuple = ()
print()
print('call the function ')
print('type "add_item_tuple(myTuple)" and press Enter')

print()

def add_item_tuple(myTuple):
   
    myList = list(myTuple)
    myList.append(item)
    newTuple = tuple(myList)
    print("the new tuple: " + str(newTuple))
    return;




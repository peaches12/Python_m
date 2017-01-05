#the program will copy the given list

list1 = ['a','b','c','d']
print('the initial list: ' + str(list1))
list2 = []
list2 = list1.copy()
list3 = []
list3 = list1 # another way to create a copy

print('the copy is:      ' + str(list2))
print('one more copy:    ' + str(list3))

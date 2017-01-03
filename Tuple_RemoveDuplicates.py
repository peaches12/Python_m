#the program will remove duplicates from tuple

mytuple = (2,2,0,0,44,44, 17, -20, -20)



print('the initial tuple:' + str(mytuple))

# turn the tuple into a list

mylist = []
mylist = list(mytuple)
print('the tuple is turned into a list:' + str(mylist))

m = 0

while m < len(mylist):
    if mylist[m] == mylist[m + 1]:
      mylist.remove(mylist[m])
    
    m = m+1
   
   


print('the final list:  ' + str(mylist))

#turn the list into a tuple
mytuple = tuple(mylist)
print()
print('---------------------------------------------')
print()

print("my new  tuple without duplicates : " + str(mytuple))

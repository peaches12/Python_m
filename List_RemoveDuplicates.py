#the program will remove duplicates from the list

mylist = [1,1,2,2,3,4,4,5,5,6,7,7]

print('the initial list:' + str(mylist))

m = 0

while m < len(mylist):
    if mylist[m] == mylist[m + 1]:
      mylist.remove(mylist[m])
    
    m = m+1
   
   


print('the final list:  ' + str(mylist))

#turn the list into a tuple
mytuple = tuple(mylist)
print("my tuple: " + str(mytuple))





    



    

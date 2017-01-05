#the program will print the items longer than required lenght

myList = ['dog','tiger','mouse', 'flamingo', 'elephant', 'snake', 'bird', 'hippopotamus']

long = int(input("Enter a number: "))
print("Call the functin 'item(myList)'")



def item(myList):
    n = 0
    while n < len(myList):
        if len(myList[n]) > long:
           print(myList[n])

        n = n + 1
    return;


        

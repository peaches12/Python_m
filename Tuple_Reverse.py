# the program will reverse a tuple


Tuple = (1,2,3,10,100)
print('the initial tuple: ' + str(Tuple))
List = []
newTuple = ()
print('type "reverse_tuple(Tuple)" and press ENTER ')

def reverse_tuple(Tuple):
    
    List = list(Tuple)
    List.reverse()
    newTuple = ()
    newTuple = tuple(List)
    print('the reversed tuple: ' + str(newTuple))
    return;
        


# the program will generate a list with random numbers and then turn it into a tuple

import random
list_random_num = []
tuple_random_num = ()

# create a function
n = int()# the number of emelents in the list, will be given by the user
low = int() # the lowest number
high = int() # the highest numner
step = int() # the step



#create a function to generate the list
def list_rand(low, high,step):
    for i in range(n):
        list_random_num.append(random.randrange(low,high,step))
    print('Your list: '+ str(list_random_num))
    print()
    return;

n = int(input("Enter the number of elements in the list: "))
low = int(input("Enter the lowest number for the list: "))
high = int(input("Enter the highest number for the list: "))
step = int(input("Enter the step: "))

#call the function           
list_rand(low,high,step)

#turn the list into the tuple
tuple_random_num = tuple(list_random_num)

print('Your tuple: ' + str(tuple_random_num) )


      






      






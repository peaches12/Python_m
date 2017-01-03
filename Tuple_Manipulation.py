tuple = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
print('My tuple: ' + str(tuple) )

print(type(tuple))
print('the lenght: ' + str(len(tuple)) + ' elements')
# find the index of the element 1
print('the index of the element 1 is: ' + str(tuple.index(1)) )

y = tuple[::-1]
print('reversed tuple: ' + str(y) )

x = tuple[0:2]
z = tuple[-3:]
v = tuple[:-4:-1]
first_four = tuple[0:4]
last_four = tuple[-4:]
first_last_four = first_four + last_four

print('sliced tuple with the first two elements: ' + str(x) )
print('sliced tuple wiht the three last elements: ' + str(z) )
print()
# print(first_four)
# print(last_four)
print('the first and the last four elements: ' + str( first_last_four) )
my_list = list(tuple)
print(my_list)
my_list.append(30)
print(my_list)
print()


new_tuple = tuple(1,2,3)
print(new_tuple)









 












      


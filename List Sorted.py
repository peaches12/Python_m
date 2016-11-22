#the program will determine if a list is sorted one or not

list1 = [2,5,1,0,-6,12,7]
list2 = list(range(0,6))
list3 = ['a','b','A','d']
list4 = ['Mary', 'John', 'Teresa', 'Angela']
print("Call the function 'sorted_list(parameter)' ")
print("Choose list1/list2/list3/list4 as the parameter")
print()

# create a function to determine, if the passed list is a sorted list

def sorted_list(list):
        if list == sorted(list):
                print('the list is sorted')
                print(list)
        else:
                print('the list is not sorted: ' + str(list))
                print()
                print('after sorting the list: ' + str(sorted(list)))
                


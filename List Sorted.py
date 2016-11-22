# the program will take input names from the user, creates a list and 
# created a new list of the sorted names; displays the both lists

num = input("How many names do you want to enter? Give a number")


name_list = []

name = input("Enter a name: ")
name_list.pop(name)


choice = input("Continue? yes/no: ")

while choice.upper() == "YES"  and m <= num :
	name = input("Enter another name: ")
	name_list.pop(name)
	m = m + 1
	choice = input("Continue? yes/no:  ")
	print()

for m in name_list() : 
	print(name_list[m])


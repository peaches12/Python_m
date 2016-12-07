# the program will count the number of strings in the list
# where the string length is 2 or more characters and
# the first and last letter are the same

list = ['a  ','sos','  b','cat','  madam ', 'dad  ', 'monom',' abba','boob', 'mat', 'tatoo', 'depend']
print(list)
print()
i = int()
n = 0
w= str()


for i in range(len(list)):
    if  len(list[i].strip(' ')) >= 2:
        w = list[i].strip(' ')# to remove all trailing whitespaces 
        if (w[0]) == (w[-1]):
            print(list[i])
            n = n + 1
            
print()
print('the number of elements')
print('with the sting lenght more then 2 characters ')
print('and the same first and last letter : ' + str(n))
print('the end')

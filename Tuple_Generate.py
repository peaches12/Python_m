# the program will create a tuple by geneimport random
import string

random_list = random.sample(range(100),10)

print(random_list)
print()

random_tuple = tuple(random_list)
print(random_tuple)
print()

random_list2 = [random.randrange(1,20,1)
                for i in range(7)
                ]
print(random_list2)
print(str(tuple(random_list2)))

print( str(''.join(random.choice(string.ascii_lowercase)
        for i in range(5)) )
      

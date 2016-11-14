# Customer list

Name = ["Mary", "John", "Sue", "Robert"]
Age = [22, 35, 16, 55]
City = ["Dallas", "Indianapolis", "Bordo", "Orlean"]

for n in range(0,4):
    print(Name[n] + " " + str(Age[n])+" years old; City: " + City[n])

print()

findCustomer = input("Enter the name of the customer (Mary,John,Sue,Robert): ")

i = Name.index(findCustomer)
#print(Name.index(findCustomer))
print("Information about " + findCustomer+ " :")

print(Name[i]+  " is " + str(Age[i]) + " years old, lives at " + City[i])



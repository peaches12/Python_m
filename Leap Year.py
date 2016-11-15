#the program will find out if the entered year is a leap year,
# divisible by 4 and 400 but not divisible by 100
# for example 1992, 1996, 2000 and 2400 are leap years


year = int(input("Enter a year here: "))

if (year%4) == 0 or  year%400 == 0:
    print("year " + str(year) + " is a leap year")
    print()
    print("------------------------------------------")
    choice = input("Do you want to continue(Yes/No): ")
    
    while choice.upper() == "YES":
        year = int(input("Enter a year here: "))
        if year%4== 0 or year%400 == 0:
            print("year " + str(year)+ " is a leap year")
            print()
            print("------------------------------------------")
            choice = input("Do you want to continue? Yes/No: ")
        else:
            print("year " + str(year) + " is not a leap year")
            print()
            print("------------------------------------------")
            choice = input("Do you want to continue(Yes/No): ")
            
    
else:
    print("year " + str(year) + " is not a leap year")
    choice = input("Do you want to continue?(Yes/No): ")
    
    while choice.upper() == "YES":
        year = int(input("Enter a year here: "))
        if year%4== 0 or year%400 == 0:
            print("year " + str(year)+ " is a leap year")
        
            choice = input("Do you want to continue? Yes/No: ")
        else:
            print("year " + str(year) + " is not a leap year")
            print()
            print("------------------------------------------")
            choice = input("Do you want to continue(Yes/No): ")
            print()
            print("------------------------------------------")

print()
print("The end")

print("************************************")



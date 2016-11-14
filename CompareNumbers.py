# Compare tree numbers

print("We will compare three different numbers")
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))
print()

if num1 > num2:
    if num1 > num3:
        print("number1 is the greatest")
    else:
        print("number3 is the greatest")
elif num1 < num2:
    if num2 > num3:
        print("number2 is the greatest")
    else:
        print("number3 is the greatest")
else:
    print("OK")

    

You are  on a long car trip and arrive at a gas station. It is 200 miles to the next station.
The program will figure out  if you need to buy gas here, or if you can wait for the next station.
The program will ask questions:
	# How big is your gas tank, in liters
	# How full is your tank (in percent, for example half full = 50 )
	# How many miles per liter does your car get


tank = int(input("Enter the capacity of your gas tank in liters: ")) 


full = int(input("Enter how full is your tank (in percent) : "))

mileage = int(input("Enter how many miles per liter your car gets: "))

distanceToRun = mileage*(tank*full/100) # the miles your car can run

distance = distanceToRun-200

 if distance<0:
	print ("You can go another " + str(distanceToRun) + " miles")
	print("The next gas station is 200 miles away")
	print("You dont' have enought gas to arrive to the next gas station")
	print("Buy gas here!")
else:
	print("You can go another " + str(distanceToRun) + " miles")
	print("The next gas station is 200 miles away")
	print("You have enouth gas to arrive to the next gas station")



# or another version 


if (mileage*(tank*full/100)-200) <0:
	print ("You can go another " + str(mileage*(tank*full/100)) + " miles")
	print("The next gas station is 200 miles away")
	print("You dont' have enought gas to arrive to the next gas station")
	print("Buy gas here!")
else:
	print("You can go another " + str(mileage*(tank*full/100)) + " miles")
	print("The next gas station is 200 miles away")
	print("You have enouth gas to arrive to the next gas station")



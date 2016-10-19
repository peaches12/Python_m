# A store is having a sale. It is giving 10% off puchases of $10 or lower, and 20% of purcahses of greater then $10.
# The program is asking the purchase price and displays the discount and the final price.

purchase = float(input("Enter the purchase amount: "))\

Enter the purchase amount: 11
>>> if purchase < 10:
	discount = purchase-purchase*0.9
	discount = '%.2f'%discount
	print("Your discount is 10% : " + discount)

	purchase = purchase*0.9
	purchase = '%.2f'%purchase
	print("You should pay: " + purchase)
else:

	discount = purchase-purchase*0.8
	discount = '%.2f'%discount
	print('Your discount is 20% : ' + discount)

	purchase = purchase*0.8
	purchase = '%.2f'%purchase
	print("You should pay: " + purchase)

	
Your discount is 20% : 2.20
You should pay: 8.80


# the program will convert the temperature to Kelvin, Celsius or Fagreheit

measure =input("Enter the temperature measure K or C or F: ")
inputTemp = float(input("Enter the temperature: "))
measureNew = input("Enter the meausure you want to convert to K or C or F: ")

resultTemp = float()


                  

                  

if measure == "K" and measureNew== "C":
                  resultTemp = inputTemp - 273.15
                  print("Answer: " + str(round(resultTemp,1)) + " C")
elif measure == "K" and measureNew == "F":
                  resultTemp = (inputTemp - 273.15) * 9/5 + 32
                  print("Answer: " + str(round(resultTemp,1)) + " F")
elif measure == "F" and measureNew == "K":
                  resultTemp =(inputTemp + 459.67)* 5/9
                  print("Answer: " + str(round(resultTemp,1)) + " K")
elif measure == "F" and measureNew == "C":
                  resultTemp = (inputTemp - 32) * 5/9
                  print("Answer: " + str(round(resultTemp,1)) + " C")
elif measure == "C" and measureNew  == "F":
                  resultTemp = (inputTemp * 9/5) + 32
                  print("Answer: " + str(round(resultTemp,1)) + "F")
elif measure == "C" and measureNew == "K":
                  resultTemp = inputTemp + 273.15
                  print("Answer: " + str(round(resultTemp,1)) + "K")
else:
                  print("Wrong entry")

                  

            
    

                

                


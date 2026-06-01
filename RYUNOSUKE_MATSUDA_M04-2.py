#process has the user enter three numbers
#Then checks if any two numbers summed add up to the third number
#add up to the third number

#initialization
num1 = 0.0
num2 = 0.0
num3 = 0.0
answer = ""

#get data
num1 = float(input("Please enter your first number: ")) 
num2 = float(input("Please enter your second number: ")) 
num3 = float(input("Please enter your third number: ")) 

#process data
if (num1 + num2) == num3:
   answer = str(num1) + " + " + str(num2) + " = " + str(num3)
elif (num2 + num3) == num1:
   answer = str(num2) + " + " + str(num3) + " = " + str(num1)
elif (num1 + num3) == num2:
    answer = str(num1) + " + " + str(num3) + " = " + str(num2)
else: 
    answer = "No combination of numbers add up one number."

#output information
print(answer)

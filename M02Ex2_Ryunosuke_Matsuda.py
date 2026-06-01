'''user enters two numbers finds the sum, difference and mult of the numbers'''
#initialization
num1 = 0.0
num2 = 0.0
sumResult = 0.0
difresult = 0.0
mulresult = 0.0

#get data
num1 = input("Please enter yor first number: ")
num1 = int(num1)

num2 = input("Please enter yor second number: ")
num2 = int(num2)


#process data
sumResult = num1 + num2
difResult = num1 - num2
mulResult = num1 * num2

num1 = str(num1)
num2 = str(num2)

sumResult = str(sumResult)
difResult = str(difResult)
mulResult = str(mulResult)

# output information
print("Your first number is " + num1 + " plus " + num2 + " equals: " + sumResult)
print("Your first number is " + num1 + " minus " + num2 + " equals: " + difResult)
print("Your first number is " + num1 + " times " + num2 + " equals: " + mulResult)

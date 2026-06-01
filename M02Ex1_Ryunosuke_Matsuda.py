'''user enters number then multiplies by 10'''
#initialization
MULTIPLIER = 10
num = 0
result = 0

#get data
num = input("Please enter a number to be multiplied by " + str(MULTIPLIER) + " ")
num = int(num)

#process data
result = num * MULTIPLIER
num = str(num)
result = str(result)
MULTIPLIER = str(MULTIPLIER)

# output information
print("Your number is " + num + " times " + MULTIPLIER + " the result is: " + result)

#pprogram accepts two numbers from the user
#comparents them and outputs one of three statements
#1.First is larger.
#2.Second is larger.
#3.Numbers are equal.

#initialization
STATEMENT1 = "First is larger."
STATEMENT2 = "Second is larger."
STATEMENT3 = "Numbers are equal."

num1 = 0.0
num2 = 0.0
answer = ""

#get data
num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))

#process data
if (num1 == num2):
    answer = STATEMENT3
elif (num1 > num2):
    answer = STATEMENT1
else:
    answer = STATEMENT2


#output information
print(answer)

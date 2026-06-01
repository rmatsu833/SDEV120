x = 0
value = 0

x = int(input("enter your number: "))

for digit in range (1, x + 1):
   value = (int(digit) ** x) + value
   
   
print("The value is " + str(value))
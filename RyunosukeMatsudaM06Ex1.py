SIZE = 10
num = []
for userInput in range(SIZE):
   num.append(int(input("Enter a number ")))
   
for count in range(SIZE - 1, -1, -1):
   print(str(num[count]))
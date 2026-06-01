SIZE = 10
num = []
smallest = 0
largest = 0

for count in range(SIZE):
   num.append(float(input("enter a number ")))
   
for count in range(SIZE):
   print(str(num[count]))
   
smallest = int(num[0])
largest = int(num[0])

for count in range(1,SIZE):
   if num[count] < smallest:
      smallest = num[count]
      
for count in range(1,SIZE):
   if num[count] > largest:
   	  largest = num[count]
   	  
print('Smallest: ' + str(smallest))
print('largest: ' + str(largest))	   
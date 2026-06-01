name = ""
employeeName = []
salary = []
salary1 = 0
salary2 = 0
quit = "zzz"
count = 0
avg = 0
sum = 0
high = 0
low = 0

name = input("Please enter your name or " + quit + " to quit: ")
while name != quit:
   employeeName.append(name)
   salary1 = float(input("Please enter your salary in even thousands: "))
   salary1 = "%0.1f" % salary1
   salary.append(salary1)
   sum += float(salary1)
   count += 1
   name = input("Please enter your name or " + quit + " to quit: ")
   
for index in range(0,len(employeeName)):
   print(employeeName[index] + "\t" + salary[index])
   
avg = sum / count
avg = "%0.1f" % avg
print("The average is " + avg + " thousands dollers.")
high = float(avg) + 5
low = float(avg) - 5

for index1 in range(0,len(salary)):
   if float(salary[index1]) < high and float(salary[index1]) > low:
      print(employeeName[index1])
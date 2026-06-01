# List a class roster of students

#initialization
SIZE = 3
firstName = []
lastName = []
count = 0

#get data
for count in range(SIZE):
   firstName.append(input("Please enter student " + str(count + 1) + "'s first name: "))
   lastName.append(input("Please enter student " + str(count + 1) + "'s last name: "))
   
print("Class list")
   
for count in range(SIZE):
   print(str(count) + lastName[count] + ", " + firstName[count])
   

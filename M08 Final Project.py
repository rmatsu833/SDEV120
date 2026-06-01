size = 9
HIGH_LEVEL = 10
MED_LEVEL = 5
LOW_LEVEL = 0
trainerName = []
numberEnrolled = []
highCount = 0
medCount = 0
lowCount = 0
count = 0
while count <= size:
   trainerName.append(input("Please enter trainer name: "))
   numberEnrolled.append(int(input("Please enter the enrolles: ")))
   count += 1
   
count = 0

while count <= size:
   if numberEnrolled[count] > HIGH_LEVEL:
      highCount += 1
      
   elif numberEnrolled[count] > MED_LEVEL:
      medCount += 1
      
   else :
      lowCount += 1
   count += 1   
      
print("Number of trainers with 11 or more enrollees: " + str(highCount))
print("Number of trainers with 5 to 10 enrollees: " + str(medCount))
print("Number of trainers with 0 to 5 enrollees: " + str(lowCount))

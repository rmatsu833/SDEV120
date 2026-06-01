#initialization
QUIT = "zzzz"
studentName = ""
studentScore = 0.0
studentCount = 0
classTotal = 0.0
classAverage = 0.0

# get and process data and write detailed report
studentName = input("Please enter student's name or " + QUIT + "to end: ")

while (studentName != QUIT):
       studentScore = float(input("Please enter " + studentName + "'s quiz score: "))
       classTotal = classTotal + studentScore
       studentCount = studentCount + 1
       print(studentName + "\t\t" + str(studentScore))
       studentName = input("Please enter student's name or " + QUIT + "to end: ")

#output information
if studentCount == 0:
    print("No student data was entered.")
else:
    classAverage = classTotal / studentCount
    print("The class's average score for this quiz is: " + str(classAverage))
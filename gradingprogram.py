#initialization
QUIT = "zzz"
NUM_PROJECTS = 4
gradeScale = [90, 80, 70, 60, 0]
studentName = [] # we use the [] squire brackets for lists
studentTotalScore = 0
studentAvgScore = []
studentLetterGrade = []
score = 0
counts = 0
name = ""
average = 0.0

#get data and process
name = input("Please enter a student's name or " + QUIT + " to end: ")
studentName.append(name)
while studentName[counts] != QUIT:
   for projectCount in range (NUM_PROJECTS):
      score = float(input("Please enter " + studentName[counts] + "'s project " + str(projectCount + 1) + " score: "))
      studentTotalScore += score
      average = studentTotalScore / NUM_PROJECTS
   studentAvgScore.append(average)
   studentTotalScore = 0
   counts += 1
   name = input("Please enter a student's name or " + QUIT + " to end: ")
   studentName.append(name)

#removes the test student from the list   
studentName.pop(-1)
   
for letterGradeCount in range(len(studentName)):
   if studentAvgScore[letterGradeCount] >= gradeScale[0]:
      studentLetterGrade.append("A")
   elif studentAvgScore[letterGradeCount] >= gradeScale[1]:	
      studentLetterGrade.append("B")
   elif studentAvgScore[letterGradeCount] >= gradeScale[2]:     
      studentLetterGrade.append("C")
   elif studentAvgScore[letterGradeCount] >= gradeScale[3]:	
      studentLetterGrade.append("D")
   else:
      studentLetterGrade.append("F")
      


#output information
for outputCount in range(len(studentName)):
   print(studentName[outputCount] + "\t" + str(studentAvgScore[outputCount]) + "\t" + studentLetterGrade[outputCount])

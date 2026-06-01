#sential value
#initialization
QUIT = "z"
SCORE_QUIT = -1
studentName = ""
studentScore = 0.0
studentTotal = 0.0
studentAvg = 0.0
quizCounter = 0

#get data
print("Name\tAverage") #output titles
studentName = input("Please enter student's name: ")
while (studentName != QUIT):
   studentScore = float(input("Please enter " + studentName + "'s score or enter " + str(SCORE_QUIT) + " to end: ")) 
   while (studentScore != SCORE_QUIT):
      studentTotal += studentScore
      quizCounter += 1
      studentName = input("Please enter student's name: ")
      studentScore = float(input("Please enter " + studentName + "'s score or enter " + str(SCORE_QUIT) + " to end: ")) 
   studentAvg = studentTotal / quizCounter
   print(studentName + ":\t" + str(studentAvg))
   studentScore = 0.0
   studentTotal = 0.0
   studentAvg = 0.0
   quizCounter = 0
   studentName = input("Please enter student's name: ")

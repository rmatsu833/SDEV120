#initialization
NUM_GAMES = 3
gameScores = []
totalScore = 0
avgScore = 0.0
count = 0

#get data
for count in range(NUM_GAMES): 
   gameScores.append(int(input("Please enter game " + str(count + 1) + " score: ")))
   totalScore = totalScore + gameScores[count]
   
#output title
print("Name\tScore")

#output detail report
for count in range(NUM_GAMES):
   print("Player's game " + str(count + 1) + " score: " + str(gameScores[count]))

#output final report
avgScore = totalScore / NUM_GAMES
print()
print("Player's total score is: " + str(totalScore))
print("Player's average score is: " + str(avgScore))

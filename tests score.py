'''
calculating student average test score
Author: Ryunosuke Matsuda
Date: 8/2/2024
Version: 1.0
'''

#initialization
NUM_TESTS = 3
test1 = 0.0
test2 = 0.0
test3 = 0.0
testsTotal = 0.0
testsAverage = 0.0

#get data
test1 = input("Please enter student's test 1 score is: ")
test2 = input("Please enter student's test 2 score is: ")
test3 = input("Please enter student's test 3 score is: ")

#test1 = float(input("Please enter student's test 1 score: "))
#cashing scores
test1 = float(test1)
test2 = float(test2)
test3 = float(test3)

#process data
testsTotal = test1 + test2 + test3
testsAverage = testsTotal / NUM_TESTS

#cashing to string for output
test1 = str(test1)
test2 = str(test2)
test3 = str(test3)
testsTotal = str(testsTotal)
testsAverage = str(testsAverage)

#output information(ECHO)
print("Student's test 1 score is: " + test1 + ".")
print("Student's test 2 score is: " + test2 + ".")
print("Student's test 3 score is: " + test3 + ".")
print("Student's testsTotal score is: " + testsTotal + ".")
print("Student's testsAverage score is: " + testsAverage + ".")


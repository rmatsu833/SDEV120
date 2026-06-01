"""
problem01
author: Ryunosuke Matsuda
Date: 1/31/24
Version:1.0
"""
# initialization
point1x = 0
point1y = 0
point2x = 0
point2y = 0
distance1 = 0.0
distance2 = 0.0

#get date
point1x = input("Please enter the x cordinate of point 1: ")
point1y = input("Please enter the y cordinate of point 1: ")

point2x = input("Please enter the x cordinate of point 2: ")
point2y = input("Please enter the y cordinate of point 2: ")

#casting to numbers
point1x = int(point1x)
point1y = int(point1y)

point2x = int(point2x)
point2y = int(point2y)

#process date
distance1 = ((point2x - point1x) ** 2) + ((point2y - point1y) ** 2) 
distance01 = (distance1 ** .5)

point2x = input("Please enter a new x cordinate of point 2: ")
point2y = input("Please enter a new y cordinate of point 2: ")

point2x = int(point2x)
point2y = int(point2y)

distance2 = ((point2x - point1x) ** 2) + ((point2y - point1y) ** 2) 
distance02 = (distance2 ** .5)

#getting ready to output information
distance001 = str(distance01)
distance002 = str(distance02)

#output information
print(" the distance from point1 to point2 is: " + distance001)
print(" the new distance from point1 to point2 is: " + distance002)

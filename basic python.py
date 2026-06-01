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
distance1 = (distance1 ** -2)

#replace information in point2x and point2y
point2x = input("Please enter the x cordinate of point 2: ")
point2y = input("Please enter the y cordinate of point 2: ")

#casting to numbers
point2x = int(point2x)
point2y = int(point2y)

#process date
distance2 = ((point2x - point1x) ** 2) + ((point2y - point1y) ** 2) 
distance2 = (distance2 ** -2)

#getting ready to output information
distance1 = str(distance1)
distance2 = str(distance2)

#output information
print(" the distance from point1 to point2 is: " + distance1)
print(" the distance from point1 to point2 is: " + distance2)

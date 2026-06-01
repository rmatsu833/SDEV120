#count up for loop

#initialization
START = 0 
END = 0
number = 0

#get data
END = float(input("Please enter a number to count up to from zero: "))
END = int(END)

#process data and write detail report
for count in range((END + 1)):
    print(str(count))
    
#output information
print("\nEND of report") 
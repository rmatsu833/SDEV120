#make a counter from 000 to 999
#initialization
TOP_NUM = 10
RESET = 0
digit1 = RESET
digit2 = RESET
digit3 = RESET

#process data
for digit1 in range(0, TOP_NUM, 1): #range(start,stop,step)
   for digit2 in range(0, TOP_NUM, 1):
     for digit2 in range(0, TOP_NUM, 1):          
        print(str(digit1) + ":" + str(digit2) + ":" + str(digit3))
            
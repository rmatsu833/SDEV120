#make a counter from 000 to 999
#initialization
TOP_NUM = 10
RESET = 0
digit1 = RESET
digit2 = RESET
digit3 = RESET

#process data
while (digit1 < TOP_NUM):
   while (digit2 < TOP_NUM):
      while (digit3 < TOP_NUM):
         print(str(digit1) + ":" + str(digit2) + ":" + str(digit3))
         digit3 += 1
      digit3 = RESET       
      digit2 += 1
   digit2 = RESET
   digit1 += 1 #it means digit1 = digit1 + 1
     
'''
@Author: Pavani
@Date: 06-11-2021 17:47:00
@Last modified by: Pavani
@Last modified time :06-11-2021 17:47:00
@Title : Number of times flip the coin and get heads and tails percentage ”

'''

import random
result = ("HEAD","TAIL")
head = 0
tail = 0
counter = 0
value = True

while (value == True):
    try:
        print("Enter the number of times you want to flip the coin :")
        flips = int(input())
        if flips>0:
            while(counter <= flips):
                output= random.choice(result)
                if(output == "HEAD"):
                     head = head + 1
                elif (output == "TAIL"):
                    tail = tail + 1
                counter = counter+1

        tailPercent = str((tail *100)/ flips)
        headPercent = str((head *100)/ flips)

        print("Head :"+headPercent,"Tail:"+tailPercent)
        break
    except Exception:
     print("hey its an error because you entered invalid input")
    finally:
        print("its flip coin program to know the heads and tail percentage")    
       
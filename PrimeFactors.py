'''
@Author: Pavani
@Date: 06-11-2021 14:49:00
@Last modified by: Pavani
@Last modified time : 06-11-2021 14:49:00
@Title : Gives prime factors of a Number ”
'''
#Following are the steps to find all prime factors. 
#1) While num is divisible by 2, print 2 and divide num by 2. 
#2)  num must be odd. Now start a loop from i = 3 to the square root of num. While i divides num, print i, and divide n by i. 
#   After i fails to divide num, increment i by 2 and continue. 
#3) If num is a prime number and is greater than 2, then num will not become 1. So print num if it is greater than 2. 

#Python has also a built-in module called math , which extends the list of mathematical functions.
# When you have imported the math module, you can start using methods and constants of the module.

import math
def primefactors(num):
    """primefactors to generate prime factors of the given number
       parameter : n
       return value : int n factors"""

    while num % 2 == 0:
        print(2)
        num = num / 2
    for i in range(3,int(math.sqrt(num))+1,2):
        while ( num % i == 0 ):
            print (i)
            num = num / i
    if num > 2:
        print (num)  
        
while True:        
 try:
  num = int(input("Enter the number to get prime factors for : "))
  print("the primefactors for ",num, ":")
  primefactors(num) 
  break
 except Exception:
    print("hey its an error because you entered invalid input")
    continue
 finally:
     print("its a primefactors program")
    



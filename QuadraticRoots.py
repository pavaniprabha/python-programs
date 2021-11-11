'''
@Author: Pavani
@Date: 07-11-2021 16:10:00
@Last Modified by: pavani
@Last modified time : 07-11-2021 16:10:00
@Title : A program that takes a,d,c from quadratic equation and print the roots”
'''

#abs() function is used to return the absolute value of a number, i.e., it will remove the negative sign of the number. 
# The abs() takes only one argument, a number whose absolute value is to be returned. The argument can be an integer, 
# a floating-point number, or a complex number.
# math is an in-build module which allows mathematical operations.

import math
def deriveroots(a,b,c):
    """to calculate roots of quadratic equation
       parameter : a,b,c
       return value : roots"""

    #To find determinent
    det = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(det))

    if det > 0:
        print("real and different")
        root1 = (-b + sqrt_val)/(2*a)
        root2 = (-b - sqrt_val)/(2*a)
        print("roots are: ", root1 , root2 )
    elif det == 0:
        print("roots are real and same")
        print("root is", -b /(2*a))
    else:
        print("roots are complex!!!") 
        
while True:
 try:         
   a = int(input("enter the x*x coefficient : "))
   b = int(input("enter the x coefficient : "))
   c = int(input("enter the constant : "))
   if (a == 0):
     print("give the correct quadratic equation")
   else:
      deriveroots(a,b,c)
   break
 except ValueError:
    print("hey its an error showing invalid input")
    continue
 finally:
    print("its an quadratic equation program")
    
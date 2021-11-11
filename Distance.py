'''
@Author: Pavani
@Date: 07-11-2021 16:55:00
@Last Modified by: Pavani
@Last modified time : 07-11-2021 16:55:00
@Title : A program that takes two integer command-line arguments x
         and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
         formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function”
'''

# math() function is used to allows mathematical calculations and it is in-build function in python.
import math
 
def calculateDistance(num1,num2):
    """to calculate distance of the point from origin
       parameter : num1,num2
       return value : distance"""

    distance = math.sqrt(num1 * num1 + num2 * num2)
    print("the distance is : " ,distance)
while True:
     try:
        num1 = int(input(print("Enter x co-ordinate")))
        num2 = int(input(print("Enter y co-ordinate")))
        calculateDistance(num1,num2)
        break
     except Exception:
        print("hey its an error because you entered invalid input")
        continue
     finally:
        print("its a distance program between point and origin")

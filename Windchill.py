'''
@Author: pavani
@Date: 07-11-2021 15:50:00
@Last Modified by: Pavani
@Last modified time : 07-11-2021 15:50:00
@Title : A program to take temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the
         National Weather Service defines the effective temperature (the wind chill) to be:
         Note: the formula is not valid if t is larger than 50 in absolute value or if v is larger
         than 120 or less than 3 (you may assume that the values you get are in that range) ”
'''


import math
def windchill(temp,speed):
    """to calculate windchill
       parameter : temp,speed
       return value : wchill value"""

    wchill = 35.74 + 0.6215 * temp -35.75 * math.pow(speed, 0.16) + 0.4275 * temp * math.pow(speed, 0.16)
    print("the wind chill is ", int(round(wchill)))
while True:
 try:
  temp = float(input("enter in fahrenheit less than 50 : "))
  speed = float(input("enter wind speed in miles per hr between 3 to 120 : "))

  if (temp > 50 or speed > 120 or speed < 3 ):
    print ("enter valid speed and temperature")
  else:
    windchill(temp,speed)
    break
 except Exception:
    print("hey its an error because you entered invalid input")
    continue
 finally:
    print("here we are calculated windchill")
'''
@Author: Pavani
@Date: 06-11-2021 13:56:00
@Last modified by: Pavani
@Last modified time : 06-11-2021 13:56:00
@Title : Print the Nth Harmonic number and N! = 0 ”
'''
# Nth harmonic number is the sum of the reciprocals of the first n natural numbers.
# harmonic numbers are the sums of the inverses of integers, forming the harmonic series.

def harmonic(num):
    """to generate harmonic value of the given number
       parameter : num
       return value : harmonic number"""

    # Base condition
    if (num < 2):
        return 1
    else:
        return 1 / num + (harmonic(num-1))    
try:
  num = int(input("enter the number :"))
  if (num == 0):
    print("given value should not be zero ")
  else:
    print("the harmonic number is", (harmonic(num)))
except Exception:
    print("hey its an error because you entered invalid input")
finally:
  print("its an harmonic number program")
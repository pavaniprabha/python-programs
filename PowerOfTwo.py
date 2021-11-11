'''
@Author: Pavani
@Date: 06-11-2021 14:21:00
@Last modified by: Pavani
@Last modified time : 06-11-2021 14:21:00
@Title :  This program takes a command-line argument N and prints a table of the
          powers of 2 that are less than or equal to 2^N.where  0 <= N < 31 ”

'''
num = int(input("Enter the number : "))
try:
 if ( num < 31):
     for i in range(num + 1):
         print(2 ** i)       #prints the power of 2 , ** means power 
 else:
     print("give the range less than 31")
except Exception:
    print("hey its an error because you entered invalid input")
finally:
    print("program to check leapyear or not")


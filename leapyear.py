'''
@Author: Pavani
@Date: 06-11-2021 13:10:00
@Last modified by: Pavani
@Last modified time : 06-11-2021 13:10:00
@Title : Given four digit year and the year is leap year or 
         not is printed  ”
'''
#A year is called a leap year if it contains an additional day which makes the number of the days in that year is 366 days.
#A leap year occurred once every 4 years.
#if year is divisible by 400 then is_leap_year
#else if year is divisible by 100 then not_leap_year
#else if year is divisible by 4 then is_leap_year
#else not_leap_year


year = int(input("enter year: "))
try:
 if((( year % 4 == 0) and ( year % 100 != 0)) or ( year % 400 == 0)):
     print (year, " is leap year")
 else: 
    print(year, "it is not a leap year")
except Exception:
    print("hey its an error because you entered invalid input")
finally:
    print("program to check leapyear or not")

     

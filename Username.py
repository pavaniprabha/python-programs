'''
@Author: Pavani
@Date: 06-11-2021 13:49:00
@Last modified by: Pavani
@Last modified time :06-11-2021 13:49:00
@Title : User Input and Replace String Template
         “Hello <<UserName>>, How are you?”
'''

# re means regualr expression(regex) which allows you to check whether a given string matches a given pattern or not

import re
str = "Hello <<UserName>>, How are you?"
try:
  name = input("enter the name :")
  if re.match("^[A-Z]{1}[a-z]{2,}$", name):
            new_str = str.replace("<<UserName>>", name)            # replace() function is used to replace the string with new string
            print(new_str) 
  else:
    print("its invalid name")          
except Exception:
    print("hey its an error because you entered invalid input")
finally:
  print("its username program")
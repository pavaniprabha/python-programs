'''
@Author: Pavani
@Date: 07-11-2021 16:35:00
@Last Modified by: Pavani
@Last modified time: 07-11-2021 16:35:00
@Title : A program that takes rows and columns to print 2d array
'''
def array_two(rows_number,columns_number):

    """to print array taking rows and columns
       parameter : rows_number,columns_number
       return value : printing matrix format"""
  
# matrix
    matrix = [] 
    print("Enter the entries row wise:") 
  
# For user input 
    for i in range(rows_number):          #  for loop for row entries 
        a =[] 
        for j in range(columns_number):      #  for loop for column entries 
            a.append(int(input())) 
        matrix.append(a) 
  
# For printing the matrix 
    print("the 2D array of ", rows_number, "and" , columns_number, "elements are :")
    for i in range(rows_number): 
        for j in range(columns_number): 
            print(matrix[i][j], end = " ") 
        print() 
       
try:
  rows_number = int(input("Enter the number of rows:")) 
  columns_number = int(input("Enter the number of columns:")) 
  array_two(rows_number,columns_number) 
except Exception:
    print("hey its an error because you entered invalid input")
finally:
     print("its 2D array program")   

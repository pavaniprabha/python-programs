'''
@Author: Pavani
@Date: 07-11-2021 17:04:00
@Last Modified by: Pavani
@Last modified time : 07-11-2021 17:04:00
@Title : A program to calculate the sum of triples equals to zero and
         print that triples
'''

# Sum of 3 integers in array should be equal to zero

def sum_zero_three(list,item):

    """to calculate the three numbers that equals to zero
       parameter : list of values and length of list .list,num_list
       return value : numbers of 3 """
    element_matched = False

    for i in range(0,item-2):            #iterate from i=0 to item-2 ,for first to last 2 digit
        for j in range(i+1,item-1):      #iterate from i+1 to item-1 , for last 1 digit        

            for k in range(j+1,item):    # for last digit

                if(list[i]+list[j]+list[k] == 0):
                    print(list[i],list[j],list[k])
                    element_matched = True
    
    if (element_matched == False):
        print("the elements given are not making zero......")
while True:        
 try:
  num = int(input("enter number of elements :"))
  list = []

  for i in range(0,num):
    elements = int(input("enter elements :"))
    list.append(elements)
  item = len(list)
  sum_zero_three(list,item)
  break
 except Exception:
    print("hey its an error because you entered invalid input")
 finally:
    print("triplets program")

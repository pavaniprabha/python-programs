'''
@Author: Pavani
@Date: 07-11-2021 17:47:00
@Last modified by: Pavani
@Last modified time : 07-11-2021 17:47:00
@Title :  Given N distinct Coupon Numbers, how many random numbers do you
          need to generate distinct coupon number? This program simulates this random
          process.

'''

import random
class Myclass:                                         # created class 

 def coupons_derivation(self):                         # initializing function  

    """Description :to calculate generated distinct coupons from the userinput
       parameter : number of coupons generated (number)
       printing value : distinct coupons and its count"""

    coupon = []
    random_numbers=0                                     #no.of random numbers which are distinct
    try:

        number=int(input("Enter The Number Of Coupons: ")) 
        print("Distinct Coupon Numbers Generated")
        for i in range(number):
            coupon_number = random.randint(10,100)       #here change in parameters
            if coupon_number not in coupon:              #Checking the number is present in list or not
                coupon.append(coupon_number)             #adding the distinct random number gnerated to list 
                random_numbers+=1
                print(coupon_number)       
                          
        print("random numbers which generated Distinct Numbers:",end = " ")
        print(random_numbers)

    except ValueError:                                      #when floating values are passed ValueError raises
        print("Invalid Input The number of coupon you want to generate should be in positive")

if __name__ == '__main__':
   obj = Myclass()                                    #object created
   obj.coupons_derivation()                           #calling fucntion with help of object
'''
@Author: Pavani
@Date: 07-11-2021 14:21:00
@Last modified by: Pavani
@Last modified time: 07-11-2021 14:21:00
@Title: Simulates a gambler who start with $stake and place fair $1 bets until
        he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
        times he/she wins and the number of bets he/she makes. 
'''
import random
class Myclass:                                       # created class

 def __init__(self,stake,goal,number):               #initialize constructor using parameter
        self.stake = stake
        self.goal = goal
        self.number = number

 def gambler(self,stake,goal,number):                #method declaration

    """Description :to calculate wins, loss and percentage of wins,loss
       parameter : stake,goal,number(amount he had,win amount,bets)
       return value : wins loss percentages and wins"""

    win_count = 0
    loss_count = 0
    counter = 0


    while (stake > 0 and stake < goal and counter < number):   
        try:
           
           counter = counter + 1
           random_generated = random.randint(0,1)    #if suppose randint() given three parameters generating type error exception
                                                     # randint() Return random integer in range [a, b], including both end points.
           if (random_generated == 1):
               win_count = win_count + 1
               self.stake = self.stake + 1
           else:
               loss_count = loss_count + 1
               self.stake = self.stake - 1
        except TypeError:
                print("error found as you entered invalid input" )                     #to find type of exception type(e).

    percent_win = (win_count/number)*100
    percent_loss = 100-percent_win
    print("Number of wins",win_count)
    print("Number of lose",loss_count)
    print("win percentage :",percent_win)
    print("loss percentage :",percent_loss )
    print("Number of times betting done",counter)

if __name__ == '__main__':                                 #main function
    stake = int(input("Enter the stake amount :"))
    goal = int(input("Enter how much money want to win : "))
    number = int(input("Enter number of times he want to get involved in betting :"))

    obj = Myclass(stake,goal,number)                       #created object of Myclass
    obj.gambler(stake,goal,number)                         #calling function with help of object
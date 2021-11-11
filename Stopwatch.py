'''
@Author: Pavani
@Date: 06-11-2021 19:10:00
@Last Modified by: Pavani
@Title :  A Stopwatch Program for measuring the time that elapses between
          the start and end clicks 
'''
import time

class Stopwatch:                       #created class
    startTime = 0
    stopTime = 0
    elapsedTime = 0
    def timeMethod(self):              #function declaration

     while True:                          #loop for the input for enter and key interruption
        
        try:                                            

            input()                      #takes input 
            startTime = time.time()
            print('time started')

        except KeyboardInterrupt:        #interruption occurs when ctrl + c

            print('time Stopped')
            endTime = time.time()
            elapsedTime = endTime - startTime
            print("Elapsed time in seconds is : ", (elapsedTime))
            break

if __name__ == '__main__':

    print("press enter to start and ctrl+c to stop time....")
    obj = Stopwatch()                     #created object
    obj.timeMethod()                      #calling fucntion with help of object
  

    
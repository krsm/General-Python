# -*- coding: utf-8 -*-
"""
Simple study related to Multithreading 

"""

import time
import threading


#function 1
def calculate_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.00000000002)
        print ('calculated square:',n*n)
        
#function 2
def calculate_cube(numbers):
    print("calculate cube numbers")
    for n in numbers:
        time.sleep(0.00000000002)
        print ('calculated cube:',n*n*n)
    
    
array_numbers = [1,2,3,4,5,6,7]



 #creatings threads
thr1 = threading.Thread(target=calculate_square,args=(array_numbers,))
thr2 = threading.Thread(target=calculate_cube,args=(array_numbers,))
    

if __name__ == "__main__":
    
    #=initial time
    t = time.time()
    #starting threads
    thr1.start()
    thr2.start()
    
    #join threads
    thr1.join()
    thr2.join()
    
    print("Executed in", time.time()-t)
    

# -*- coding: utf-8 -*-
"""
Simple study related do threads

"""

import _thread as thread
import time

# Example 1
def son(tid):

    print("Executing son", tid)

def father():

    k = 0
    while True:
        k = k + 1
        thread.start_new_thread(son, (k,))
        if input() == "q":break


# Example 2
def counter(myId, count):
    for i in range(count):
        time.sleep(1)
        print('[%s] => %s' % (myId,i))

if __name__ == "__main__":

    # Example 1
    # father()

    # Example 2
    for i in range(5):
        thread.start_new_thread(counter,(i,5))

    time.sleep(5)
    print("Exiting main thread")
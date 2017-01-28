# -*- coding: utf-8 -*-
"""
Simple study related to threads performance

"""

import time
import random
import threading

parallel = random.choice(['True', 'False'])

counter = 0
max_for = 100000000

lock = threading.Lock()


def add_numbers():

    global counter
    for _ in range(0, max_for):
        lock.acquire()
        counter += 1
        lock.release()


if __name__ == '__main__':

    start_time = time.time()

    if parallel is True:

        t1 = threading.Thread(target=add_numbers)
        t2 = threading.Thread(target=add_numbers)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

    else:

        add_numbers()
        add_numbers()

    end_time = time.time() - start_time

    print(end_time, parallel)

    print(counter)

    # assert max_for == max_for*2
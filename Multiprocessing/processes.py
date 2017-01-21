# -*- coding: utf-8 -*-
"""
Simple study related to Multiprocessing

"""

import os
from multiprocessing import Process

#function 1
def calculate_square(n):
    print('calculated square:', n*n)
    proc = os.getpid()
    print('{0} process id:'.format(proc))


#function 2
def calculate_cube(n):
    print('calculated cube:', n*n*n)
    proc = os.getpid()
    print('{0} process id'.format(proc))


if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5]
    procs = []

    for index, n in enumerate(numbers):
        p = Process(target=calculate_square, args=(n,))
        procs.append(p)
        p.start()
    #
    # for proc in procs:
    #     proc.join()

# -*- coding: utf-8 -*-
"""

Simple study related to iterators and generators

"""


import random

# Example 1
def throw_dices(n):

    dices = []
    for _ in range(0, n):
        dices.append(random.randint(1, 6))
    return dices

# Example 2
class Trhow_Dices(object):

    def __init__(self, n):
        self.n = n
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.n:
            self.counter += 1
            return random.randint(1, 6)
        else:
            raise StopIteration

def throw_dices_yield(n):

    # yield blocks function execution until next method is called

    print('starting function')
    for _ in range(0, n):
        print('starting for loop')
        yield random.randint(1, 6)
        print('exit for loop')
    print('end of function')


if __name__ == '__main__':

    # Example 1
    for dices in throw_dices(1):
        print(dices)

    # Example 2
    for dices in Trhow_Dices(1):
        print(dices)

    #Example 3
    for dices in throw_dices_yield(10):
        print(dices)
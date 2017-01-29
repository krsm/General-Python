# -*- coding: utf-8 -*-
"""

Simple study related to Queue

"""
import queue

counter = 0
max_for = 1000

# Example 1
def add_numbers(task_name):

    global counter
    for _ in range(0, max_for):
        print('Executing {}'.format(task_name))
        counter += 1
        yield


if __name__ == '__main__':


    # Example 1
    q = queue.Queue()
    q.put(add_numbers('task1'))
    q.put(add_numbers('task2'))

    while not q.empty():
        # get removes element of queue
        task = q.get()
        try:
            next(task)
        except StopIteration:
            pass
        else:
            q.put(task)

    print(counter)

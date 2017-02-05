# -*- coding: utf-8 -*-
"""
simple study about how to use pickle

"""

import pickle


def create_pkl():

    try:
        setup = pickle.load(file='setup.pkl')
        print(setup)
    except Exception as e:
        print('Exception', e)
        setup = {'timeout': 10,
                 'server': '10.0.0.1',
                 'port': 80
                 }
        output = open('setup.pkl', 'wb')
        pickle.dump(setup, output)

if __name__ == "__main__":

    create_pkl()
    print('Pickle created')






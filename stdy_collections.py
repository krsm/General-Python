# -*- coding: utf-8 -*-
"""
simple study of collections

"""
import collections


Person = collections.namedtuple('Person', 'name age gender')


if __name__ == "__main__":

    print('Type of person:', type(Person))
    Jay = Person(name='Jay', age=30, gender='male')
    Jane = Person(name='Jane', age=20, gender='female')

    for person in [Jane, Jay]:
        print(person.name, person.age, person.gender)
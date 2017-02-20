# -*- coding: utf-8 -*-
"""

Simple study related to pytest

"""


class InsufficientAmount(Exception):
    pass


class BankAccount(object):

    def __init__(self, initial_amount=0):
        self.current_balance = initial_amount

    def withdrawal_cash(self, amount):
        if self.current_balance < amount:
            raise InsufficientAmount("Not enough cash to spend!{}".format(amount))
        self.current_balance -= amount

    def deposit_cash(self, amount):
        self.current_balance += amount

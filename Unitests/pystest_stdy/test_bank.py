# -*- coding: utf-8 -*-
"""

Simple study related to pytest

"""

import pytest
from Unitests.pystest_stdy.bank import BankAccount, InsufficientAmount


def test_default_initial_amount():
    bank_account = BankAccount()
    assert bank_account.current_balance == 0


def test_setting_initial_amount():
    bank_account = BankAccount(100)
    assert bank_account.current_balance == 100


def test_bank_account_deposit_cash():
    bank_account = BankAccount(100)
    bank_account.deposit_cash(90)
    assert bank_account.current_balance == 190


def test_bank_account_withdrawal_cash():
    bank_account = BankAccount(100)
    bank_account.withdrawal_cash(90)
    assert bank_account.current_balance == 10


def test_bank_account_raises_exception():
    bank_account = BankAccount()
    with pytest.raises(InsufficientAmount):
        bank_account.withdrawal_cash(100)

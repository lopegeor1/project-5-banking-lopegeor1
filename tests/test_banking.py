"""
The test module for Account and Transaction
"""
import datetime as dt
import ast
from banking import Account, Transaction
def test_default_timestamp_now():
    """
    Given no user input defined for timestamp, the default current timestamp
    now() is used when the Transaction object is created.  The now() value should
    very similar or the same.
    """
    now = dt.datetime.now()
    trans_one = Transaction(100)
    assert trans_one.timestamp >= now

def test_userdefined_timestamp():
    """
    Given a user defined input for timestamp, the default current timestamp
    now() is not used when the Transaction object is created. The user defined
    timestamp is bound to the Transaction object using self.timestamp = timestamp.
    """
    arg_timestamp = dt.datetime(2018, 1, 10)
    trans_one = Transaction(100, arg_timestamp)
    assert trans_one.timestamp == arg_timestamp

def test_str_instance():
    """
    Given __str__(), a string respresentation of the object can be created.
    """
    trans_one = Transaction(500, dt.datetime(2018, 1, 10))
    assert str(trans_one) == '2018-01-10: +$500.00'

def test_repr_instance():
    """
    Given __repr__(), an expression is created that can be used to recreate object.
    """
    trans_two = Transaction(500, dt.datetime(2018, 1, 10))
    trans_three = trans_two #recreate trans_two instance as trans_three directly using __repr__()
    assert trans_two == trans_three

def test_negative_deposits_converted_to_positive():
    """
    Given a negative amount argument for deposit, the amount value is converted
    to positive.
    """
    account = Account()
    amount = -300
    account.deposit(amount)
    assert account.get_balance() == 300

def test_deposit_appended_to_transactions():
    """The deposit instance is appended to transactions"""
    account = Account()
    account.deposit(-300)
    account.deposit(100)
    account.deposit(30.59)
    # all of the deposit instances or 'transactions' are included Account(object)
    data = ast.literal_eval(repr(account.transactions))
    assert sum(row[0] for row in data) == 430.59

def test_withdrawal_converted_to_negative():
    """
    Given a positive amount argument for deposit, the amount value is converted
    to negative.
    """
    account = Account()
    amount = 80
    account.withdraw(amount)
    assert account.get_balance() == -80

def test_withdrawal_appended_to_transactions():
    """The withdraw instance is appended to transactions"""
    account = Account()
    account.deposit(-300)
    account.withdraw(80)
    account.withdraw(120)
    # all of the withdraw instances or 'transactions' should be in Account(object)
    data = ast.literal_eval(repr(account.transactions))
    assert account.get_balance() == sum(row[0] for row in data)

def test_no_transactions_return_0_balance():
    """Given no transaction instances, the balance should be 0"""
    account = Account()
    data = ast.literal_eval(repr(account.transactions))
    # there are neither any previous deposit or withdraw transactions
    assert sum(row[0] for row in data) == 0

def test_account_balance_series_of_transactions():
    """
    Given some transaction instances, the balance should be the sum total
    of all transacation instances
    """
    acc = Account()
    acc.deposit(100)
    acc.withdraw(90)
    acc.deposit(10)
    data = ast.literal_eval(repr(acc.transactions))
    assert sum(row[0] for row in data) == 20

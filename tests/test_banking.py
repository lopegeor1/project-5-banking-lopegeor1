"""
The test module for Account and Transaction
"""
import datetime as dt

from banking import Transaction

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

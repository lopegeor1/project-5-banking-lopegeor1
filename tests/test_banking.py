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

"""Assignment 5: Bank Account"""
import datetime as dt
class Transaction:
    """
    A transaction class represents a monetary transaction event.
    It has two properties: an amount, and a timestamp.
    """
    # Transaction is constructed with a required 'amount' argument however the initialized
    # timestamp is either None by default (current datetime is used) or a user defined
    # datetime value entered for the timestamp argument for every new Transaction() object.
    def __init__(self, amount, timestamp=None):
        self.amount = amount
        if not isinstance(timestamp, dt.datetime):
            self.timestamp = dt.datetime.now()
        else:
            self.timestamp = timestamp

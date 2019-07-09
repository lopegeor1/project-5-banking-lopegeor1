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

    def __str__(self):
        """Returns transaction with timestamp."""
        dt_formatted = '{:%Y-%m-%d}'.format(self.timestamp)
        if self.amount < 0:
            amt_formattted = '-${0:.2f}'.format(self.amount * -1)
        elif self.amount > 0:
            amt_formattted = '+${0:.2f}'.format(self.amount)
        else:
            amt_formattted = '${0:.2f}'.format(self.amount)
        # Returns amount, time of transaction.
        return f'{dt_formatted}: {amt_formattted}'

    def __repr__(self):
        """Returns expression which can be used to recreate this object."""
        dt_formatted = '{:%Y, %#m, %#d}'.format(self.timestamp)
        # Returns amount, time of transaction.
        # this string can be copy & paste to interpreter to reproduce similar instance...
        return f'Transaction({self.amount}, dt.datetime({dt_formatted}))'

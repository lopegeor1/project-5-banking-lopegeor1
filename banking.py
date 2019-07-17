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
        dt_formatted = '{:%Y_%#m_%#d}'.format(self.timestamp)
        # Returns amount, time of transaction.
        # String formatted especially to handle return sum of all transactions
        return f'[{self.amount}, ({dt_formatted})]'

class Account:
    """
    The account class represents a bank account.
    It is constructed without any arguments.
    """
    # Account is constructed without any arguments however the initialized
    # balance is zero or $0.00 for every new Account() object.
    def __init__(self):
        # amount = 0.00 -> Account() object is initialized with zero amount
        # balance = 0.00 -> Account() object is initialized with zero balance
        # self.my_list = [] -> self.transations
        self.transactions = [] # array stores list of all transacations on Account() object
        self.balance = 0.00 # self.balance added solely for testing purposes

    def deposit(self, amount):
        """make deposit to account"""
        #ensure deposit amount is converted to a positive value
        if amount < 0:
            amount = amount * -1
        transaction = Transaction(amount)
        self.transactions.append(transaction)
        self.balance += amount
    def withdraw(self, amount):
        """make withdrawal from account"""
        if amount < 0:
            amount = amount * -1
        #if (sum(row[1] for row in self.transactions) - amount) < 0:
        if (self.balance - amount) < 0:
        #if (sum(self.transactions) - amount) < 0:
            print("Warning: account in overdrawn position \nCheck account balance!")
        #ensure withdraw amount is converted to a negative value
        amount = amount * -1
        transaction = Transaction(amount)
        self.transactions.append(transaction)
        self.balance += amount

    def get_balance(self):
        """display the current balance in account object"""
        # return the current value of the balance
        #balance = '{0:.2f}'.format(sum(self.transactions))
        return round(self.balance, 2) * 1.00


    def get_transactions(self):
        """display list of transations in account object"""
        my_list = self.transactions
        #for my_list in range(len(my_list)):
        print('\n'.join(map(str, my_list)))

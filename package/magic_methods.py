"""
Demo of magic methods
"""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __str__(self):
        return f"Bank account of {self.owner}"


account_paul = BankAccount("Paul", 100)
account_joris = BankAccount("Joris", 50)


print(account_paul > account_joris)


100 > 50

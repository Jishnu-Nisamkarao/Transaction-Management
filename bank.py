# bank.py
from account import Account

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner_name, initial_balance=0.0):
        account_number = str(len(self.accounts) + 1).zfill(6)
        if account_number in self.accounts:
            account_number = str(len(self.accounts) + 2).zfill(6)
            
        new_account = Account(account_number, owner_name, initial_balance)
        self.accounts[account_number] = new_account
        return new_account

    def find_account(self, account_number):
        return self.accounts.get(account_number)

    def get_all_accounts(self):
        return self.accounts.values()
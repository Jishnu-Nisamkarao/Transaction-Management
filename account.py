# account.py
import datetime

class Account:
    def __init__(self, account_number, owner_name, initial_balance=0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance
        self.transactions = [] 
        if initial_balance > 0:
            self.transactions.append({
                'type': 'initial_deposit',
                'amount': initial_balance,
                'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append({ 
                'type': 'deposit',
                'amount': amount,
                'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            return True, f"Deposit of ${amount:.2f} successful."
        return False, "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transactions.append({  
                    'type': 'withdraw',
                    'amount': amount,
                    'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                return True, f"Withdrawal of ${amount:.2f} successful."
            return False, "Insufficient funds."
        return False, "Withdrawal amount must be positive."

    def get_details(self):
        return (f"Account Number: {self.account_number}\n"
                f"Owner: {self.owner_name}\n"
                f"Balance: ${self.balance:.2f}")

    def get_transaction_history(self):
        history_str = ""
        for transaction in self.transactions:
            history_str += (f"Type: {transaction['type'].capitalize()}, "
                            f"Amount: ${transaction['amount']:.2f}, "
                            f"Date: {transaction['date']}\n")
        return history_str if history_str else "No transactions yet."
# gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from bank import Bank

class BankingApp:
    def __init__(self, root):
        self.bank = Bank()
        self.root = root
        self.root.title("Python Banking System")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Style configuration
        self.style = ttk.Style()
        self.style.configure("TFrame", background= "white")
        self.style.configure("TLabel", background="white", font=("Helvetica", 12))
        self.style.configure("TButton", font=("Helvetica", 10, "bold"), padding=10)
        self.style.configure("Title.TLabel", font=("Helvetica", 18, "bold"), background="white", foreground="#ED0B0B")

        self.main_frame = ttk.Frame(self.root, padding="20 20 20 20")
        self.main_frame.pack(fill="both", expand=True)

        self.create_main_menu()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def create_main_menu(self):
        self.clear_frame()
        ttk.Label(self.main_frame, text="Main Menu", style="Title.TLabel").pack(pady=(0, 20))
        
        buttons_frame = ttk.Frame(self.main_frame)
        buttons_frame.pack(fill='x', padx=50, pady=5)

        ttk.Button(buttons_frame, text="Create Account", command=self.create_account_menu).pack(fill='x', pady=5)
        ttk.Button(buttons_frame, text="Deposit", command=self.deposit_menu).pack(fill='x', pady=5)
        ttk.Button(buttons_frame, text="Withdraw", command=self.withdraw_menu).pack(fill='x', pady=5)
        ttk.Button(buttons_frame, text="List All Accounts", command=self.list_accounts_menu).pack(fill='x', pady=5)
        ttk.Button(buttons_frame, text="View Transactions", command=self.view_transactions_menu).pack(fill='x', pady=5)
        ttk.Button(buttons_frame, text="Exit", command=self.root.quit, style="TButton").pack(fill='x', pady=10)

    def create_account_menu(self):
        self.clear_frame()
        ttk.Label(self.main_frame, text="Create Account", style="Title.TLabel").pack(pady=(0, 20))

        ttk.Label(self.main_frame, text="Owner Name:").pack()
        self.name_entry = ttk.Entry(self.main_frame)
        self.name_entry.pack(pady=(0, 10))

        ttk.Label(self.main_frame, text="Initial Deposit (optional):").pack()
        self.initial_deposit_entry = ttk.Entry(self.main_frame)
        self.initial_deposit_entry.pack(pady=(0, 20))

        ttk.Button(self.main_frame, text="Create", command=self.handle_create_account).pack(pady=5)
        ttk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_menu).pack(pady=5)

    def handle_create_account(self):
        owner_name = self.name_entry.get()
        initial_deposit_str = self.initial_deposit_entry.get()
        initial_deposit = 0.0

        if not owner_name:
            messagebox.showerror("Error", "Owner name is required.")
            return

        try:
            if initial_deposit_str:
                initial_deposit = float(initial_deposit_str)
                if initial_deposit < 0:
                    raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Invalid initial deposit amount.")
            return

        account = self.bank.create_account(owner_name, initial_deposit)
        messagebox.showinfo("Success", f"Account created successfully!\nAccount Number: {account.account_number}")
        self.create_main_menu()

    def deposit_menu(self):
        self.clear_frame()
        ttk.Label(self.main_frame, text="Deposit", style="Title.TLabel").pack(pady=(0, 20))

        ttk.Label(self.main_frame, text="Account Number:").pack()
        self.acc_num_entry = ttk.Entry(self.main_frame)
        self.acc_num_entry.pack(pady=(0, 10))

        ttk.Label(self.main_frame, text="Amount to Deposit:").pack()
        self.amount_entry = ttk.Entry(self.main_frame)
        self.amount_entry.pack(pady=(0, 20))

        ttk.Button(self.main_frame, text="Deposit", command=self.handle_deposit).pack(pady=5)
        ttk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_menu).pack(pady=5)

    def handle_deposit(self):
        acc_num = self.acc_num_entry.get()
        amount_str = self.amount_entry.get()

        try:
            amount = float(amount_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")
            return

        account = self.bank.find_account(acc_num)
        if account:
            success, message = account.deposit(amount)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "Account not found.")
        
        self.create_main_menu()

    def withdraw_menu(self):
        self.clear_frame()
        ttk.Label(self.main_frame, text="Withdraw", style="Title.TLabel").pack(pady=(0, 20))

        ttk.Label(self.main_frame, text="Account Number:").pack()
        self.acc_num_entry = ttk.Entry(self.main_frame)
        self.acc_num_entry.pack(pady=(0, 10))

        ttk.Label(self.main_frame, text="Amount to Withdraw:").pack()
        self.amount_entry = ttk.Entry(self.main_frame)
        self.amount_entry.pack(pady=(0, 20))

        ttk.Button(self.main_frame, text="Withdraw", command=self.handle_withdraw).pack(pady=5)
        ttk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_menu).pack(pady=5)

    def handle_withdraw(self):
        acc_num = self.acc_num_entry.get()
        amount_str = self.amount_entry.get()

        try:
            amount = float(amount_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")
            return

        account = self.bank.find_account(acc_num)
        if account:
            success, message = account.withdraw(amount)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "Account not found.")
        
        self.create_main_menu()

    def list_accounts_menu(self):
        self.clear_frame()
        ttk.Label(self.main_frame, text="All Accounts", style="Title.TLabel").pack(pady=(0, 20))

        accounts_text = "No accounts found."
        if self.bank.get_all_accounts():
            accounts_text = "\n\n".join([acc.get_details() for acc in self.bank.get_all_accounts()])
        
        accounts_label = ttk.Label(self.main_frame, text=accounts_text, justify=tk.LEFT)
        accounts_label.pack(fill='both', expand=True, padx=10, pady=10)

        ttk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_menu).pack(pady=10)

    def view_transactions_menu(self):
        self.clear_frame()
        ttk.Label(self.main_frame, text="View Transactions", style="Title.TLabel").pack(pady=(0, 20))

        ttk.Label(self.main_frame, text="Account Number:").pack()
        self.acc_num_entry = ttk.Entry(self.main_frame)
        self.acc_num_entry.pack(pady=(0, 10))

        ttk.Button(self.main_frame, text="Show Transactions", command=self.handle_view_transactions).pack(pady=5)
        ttk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_menu).pack(pady=5)

    def handle_view_transactions(self):
        acc_num = self.acc_num_entry.get()
        account = self.bank.find_account(acc_num)

        if account:
            history = account.get_transaction_history()
            messagebox.showinfo("Transaction History", f"History for Account #{acc_num}:\n\n{history}")
        else:
            messagebox.showerror("Error", "Account not found.")
        
        self.create_main_menu()

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()
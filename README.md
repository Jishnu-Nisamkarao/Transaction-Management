# Transaction Management Banking System

A simple banking transaction system with a graphical user interface (GUI) built using Python and the Tkinter library. This project simulates core banking functionalities such as creating accounts, depositing/withdrawing funds, and viewing transaction history.

## Features

- **Create Account**: Open a new bank account with a unique account number and an optional initial deposit.
- **Deposit**: Add funds to a specified account.
- **Withdraw**: Remove funds from a specified account, with checks for insufficient balance.
- **List All Accounts**: View a list of all existing accounts, including their numbers, owner names, and current balances.
- **View Transactions**: Check the detailed transaction history for any given account.
- **GUI**: User-friendly graphical interface built with Tkinter for easy interaction.

## Requirements

To run, Python installation (version 3.6 or higher). All required libraries, including Tkinter, are part of Python's standard distribution.

- **Python 3.x**

No external packages need to be installed via `pip`.

## How to Run the Project

Follow these simple steps to get the application running on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Jishnu-Nisamkarao/Transaction-Management.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Transaction Management
    ```
3.  **Run the main application file:**
    ```bash
    python gui.py
    ```

The banking application GUI will pop up, and we can start using the system.

## Project Structure

- `account.py`: Defines the `Account` class, which handles account-specific details and operations like deposits and withdrawals.
- `bank.py`: Defines the `Bank` class, which acts as a database to manage all `Account` objects.
- `gui.py`: The main application file that creates and manages the graphical user interface using Tkinter.

## License

This project is licensed under the MIT License.

---

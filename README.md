# Transaction Management Banking System

A simple banking transaction system with a graphical user interface (GUI) built using Python and the Tkinter library. This project simulates core banking functionalities such as creating accounts, depositing/withdrawing funds, and viewing transaction history.

## Features

- **Create Account**: Open a new bank account with a unique account number and an optional initial deposit.
- **Deposit**: Add funds to a specified account.
- **Withdraw**: Remove funds from a specified account, with checks for insufficient balance.
- **List All Accounts**: View a list of all existing accounts, including their numbers, owner names, and current balances.
- **View Transactions**: Check the detailed transaction history for any given account.
- **GUI**: User-friendly graphical interface built with Tkinter for easy interaction.

## Project Structure

- `account.py`: Defines the `Account` class, which handles account-specific details and operations like deposits and withdrawals.
- `bank.py`: Defines the `Bank` class, which acts as a database to manage all `Account` objects.
- `gui.py`: The main application file that creates and manages the graphical user interface using Tkinter.


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

## Screenshots
<img width="789" height="559" alt="image" src="https://github.com/user-attachments/assets/e90bd7ec-857b-4dfa-97bf-9bfb6f3ae3ad" />

1. Create Account
<img width="841" height="371" alt="image" src="https://github.com/user-attachments/assets/023fff71-00d2-44f0-b0eb-bc70941a3600" />

2. Deposit
<img width="830" height="346" alt="image" src="https://github.com/user-attachments/assets/f65cca35-13ad-46fe-9f5d-e225ed242295" />

3. Withdraw
<img width="799" height="352" alt="image" src="https://github.com/user-attachments/assets/6bc3156f-d550-4971-8c5e-8a2dcbd5a60e" />

4. List all accounts
<img width="736" height="558" alt="image" src="https://github.com/user-attachments/assets/b01478a3-25f7-435f-9092-01b7baae8792" />

5. View Trasactions
<img width="742" height="443" alt="image" src="https://github.com/user-attachments/assets/19df4154-366a-4c3a-a6df-b5c0f87a92f5" />


[![Screenshot of Banking App](https://raw.githubusercontent.com/Jishnu-Nisamkarao/Transaction-Management/main/images/thumbnail.png)](https://raw.githubusercontent.com/Jishnu-Nisamkarao/Transaction-Management/main/images/full-screenshot.png)

## License

This project is licensed under the MIT License.


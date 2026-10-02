# 💰 Financial Risk and Expense Tracker

A simple Python-based project to calculate savings, weekly expense limits, and track monthly expenses.  
This project is split into two files for modularity:

- **expense_tracker.py** → Calculates savings and remaining income after saving 20% of monthly income.
- **total_expense.py** → Imports the function from `expense_tracker.py`, collects itemized expenses, and calculates total monthly spending.

---

## 📂 Project Structure

Financial risk and expense tracker/
│
├── expense_tracker.py   # Defines Rest_amount() function
├── total_expense.py     # Uses Rest_amount() and calculates expenses
└── README.md            # Documentation


---

## ⚙️ How It Works

### 1. `expense_tracker.py`
- Asks for monthly income.
- Deducts 20% for savings.
- Shows remaining income and weekly expense target.
- Returns the remaining amount for use in other files.

### 2. `total_expense.py`
- Imports `Rest_amount()` from `expense_tracker.py`.
- Calls the function to get remaining income.
- Lets the user enter item names and prices until they press **Enter**.
- Calculates:
  - Total monthly expense
  - Remaining balance after expenses

---

## ▶️ Running the Program

Open terminal in the project folder and run:

```bash

python total_expense.py


This will:

Ask for your monthly income.

Show savings and weekly expense target.

Ask for itemized expenses.

Display total expense and remaining balance.

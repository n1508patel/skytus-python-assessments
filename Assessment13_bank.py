import json
import os
import random
from datetime import datetime

FILE = "bank_data.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def create_account(data):
    print("\n--- Create New Account ---")
    name = input("Enter your name: ").strip()
    pin = input("Set a 4-digit PIN: ").strip()
    if not pin.isdigit() or len(pin) != 4:
        print("⚠️  PIN must be 4 digits.")
        return
    acc_no = str(random.randint(100000000, 999999999))
    initial = float(input("Initial deposit (₹): "))
    data[acc_no] = {
        "name": name, "pin": pin, "balance": initial,
        "transactions": [{"type": "Initial Deposit", "amount": initial,
                          "date": datetime.now().strftime("%d-%m-%Y %H:%M")}]
    }
    save_data(data)
    print(f" Account created! Account No: {acc_no}")

def login(data):
    acc_no = input("Enter Account Number: ").strip()
    if acc_no not in data:
        print(" Account not found.")
        return None
    pin = input("Enter PIN: ").strip()
    if data[acc_no]["pin"] != pin:
        print(" Wrong PIN.")
        return None
    print(f" Welcome, {data[acc_no]['name']}!")
    return acc_no

def deposit(data, acc_no):
    amount = float(input("Enter deposit amount (₹): "))
    if amount <= 0:
        print("  Invalid amount.")
        return
    data[acc_no]["balance"] += amount
    data[acc_no]["transactions"].append(
        {"type": "Deposit", "amount": amount,
         "date": datetime.now().strftime("%d-%m-%Y %H:%M")})
    save_data(data)
    print(f" Deposited ₹{amount}. Balance: ₹{data[acc_no]['balance']:.2f}")

def withdraw(data, acc_no):
    amount = float(input("Enter withdrawal amount (₹): "))
    if amount > data[acc_no]["balance"]:
        print(" Insufficient balance.")
        return
    data[acc_no]["balance"] -= amount
    data[acc_no]["transactions"].append(
        {"type": "Withdrawal", "amount": amount,
         "date": datetime.now().strftime("%d-%m-%Y %H:%M")})
    save_data(data)
    print(f" Withdrawn ₹{amount}. Balance: ₹{data[acc_no]['balance']:.2f}")

def account_menu(data, acc_no):
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Transactions\n5. Logout")
        choice = input("Choice: ")
        if choice == "1":
            print(f"💰 Balance: ₹{data[acc_no]['balance']:.2f}")
        elif choice == "2":
            deposit(data, acc_no)
        elif choice == "3":
            withdraw(data, acc_no)
        elif choice == "4":
            for t in data[acc_no]["transactions"]:
                print(f"  {t['date']} | {t['type']} | ₹{t['amount']}")
        elif choice == "5":
            break

def main():
    print("=" * 40)
    print("      Bank Management System")
    print("=" * 40)
    data = load_data()
    while True:
        print("\n1. Create Account\n2. Login\n3. Exit")
        choice = input("Choice: ")
        if choice == "1":
            create_account(data)
        elif choice == "2":
            acc_no = login(data)
            if acc_no:
                account_menu(data, acc_no)
        elif choice == "3":
            print(" Goodbye!")
            break

if __name__ == "__main__":
    main()
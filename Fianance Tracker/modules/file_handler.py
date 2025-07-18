import csv
import os
from datetime import datetime

DATA_FILE = "data/expenses.csv"

# Ensure the CSV file exists and has headers
def initialize_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])
        print("📁 expenses.csv file created.")

# Add a new expense entry
def add_expense(date, category, amount):
    with open(DATA_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print("✅ Expense added successfully!")

# Read all expenses from file
def read_expenses():
    expenses = []
    with open(DATA_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Amount'] = float(row['Amount'])  # Convert amount to float
            expenses.append(row)
    return expenses

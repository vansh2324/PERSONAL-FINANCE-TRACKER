import pandas as pd
from datetime import datetime

DATA_FILE = "data/expenses.csv"

# Load CSV using pandas
def load_expenses():
    try:
        df = pd.read_csv(DATA_FILE)
        df['Amount'] = df['Amount'].astype(float)
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df.dropna(inplace=True)
        return df
    except Exception as e:
        print(" Error loading expenses:", e)
        return pd.DataFrame()

# Total expenses
def get_total_expenses():
    df = load_expenses()
    return df['Amount'].sum()

# Category-wise expenses
def get_expenses_by_category():
    df = load_expenses()
    return df.groupby("Category")["Amount"].sum()

# Monthly expenses
def get_monthly_expenses():
    df = load_expenses()
    df['Month'] = df['Date'].dt.strftime('%Y-%m')
    return df.groupby("Month")["Amount"].sum()

# Highest spending day
def get_max_spend_day():
    df = load_expenses()
    return df.groupby("Date")["Amount"].sum().idxmax()

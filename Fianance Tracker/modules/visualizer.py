import pandas as pd
import matplotlib.pyplot as plt
from modules.analyzer import load_expenses

# Pie chart: Category-wise expenses
def show_category_pie_chart():
    df = load_expenses()
    if df.empty:
        print("No data to visualize.")
        return

    category_data = df.groupby("Category")["Amount"].sum()
    category_data.plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title("📊 Expenses by Category")
    plt.ylabel("")  # hide y-label
    plt.tight_layout()
    plt.show()

# Line chart: Monthly expenses trend
def show_monthly_trend_chart():
    df = load_expenses()
    if df.empty:
        print("No data to visualize.")
        return

    df['Month'] = df['Date'].dt.strftime('%Y-%m')
    monthly_data = df.groupby("Month")["Amount"].sum()
    monthly_data.plot(marker='o')
    plt.title("📈 Monthly Expense Trend")
    plt.xlabel("Month")
    plt.ylabel("Amount Spent")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

import json
import os
from modules.analyzer import load_expenses

BUDGET_FILE = "data/budget.json"

# Save user budget
def set_budget(limit):
    data = {"monthly_budget": limit}
    with open(BUDGET_FILE, "w") as f:
        json.dump(data, f)
    print(f"✅ Monthly budget of ₹{limit} has been set.")

# Load saved budget
def get_budget():
    if os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, "r") as f:
            data = json.load(f)
            return data.get("monthly_budget", 0)
    return 0

# Check current month spending vs budget
def check_budget_status():
    budget = get_budget()
    if not budget:
        print("⚠️ No budget set. Please set it first.")
        return

    df = load_expenses()
    if df.empty:
        print("No expenses found to compare with budget.")
        return

    # Filter current month
    df['Month'] = df['Date'].dt.strftime('%Y-%m')
    current_month = df['Month'].max()
    current_month_expenses = df[df['Month'] == current_month]['Amount'].sum()

    print(f"📅 Current Month: {current_month}")
    print(f"💰 Your Budget: ₹{budget}")
    print(f"📉 Spent So Far: ₹{current_month_expenses:.2f}")

    if current_month_expenses > budget:
        print("🚨 Budget Exceeded!")
    elif current_month_expenses > 0.9 * budget:
        print("⚠️ You’re very close to exceeding your budget!")
    else:
        print("✅ You're within your budget.")

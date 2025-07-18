import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from modules.analyzer import load_expenses

def predict_next_month_expense():
    df = load_expenses()

    if df.empty:
        print("❌ Not enough data to make a prediction.")
        return

    df['Month'] = df['Date'].dt.to_period('M').astype(str)
    monthly_totals = df.groupby('Month')['Amount'].sum().reset_index()

    if len(monthly_totals) < 2:
        print("⚠️ Need expenses in at least 2 months to predict.")
        return

    monthly_totals['Month_Num'] = np.arange(1, len(monthly_totals) + 1)
    X = monthly_totals[['Month_Num']]
    y = monthly_totals['Amount']

    model = LinearRegression()
    model.fit(X, y)

    next_month = pd.DataFrame([[len(monthly_totals) + 1]], columns=["Month_Num"])
    prediction = model.predict(next_month)[0]

    print("\n🔮 Predicted Total Expense for Next Month:")
    print(f"💰 Estimated: ₹{prediction:.2f}")

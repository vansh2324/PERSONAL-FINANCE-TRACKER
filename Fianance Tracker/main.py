from modules.file_handler import initialize_file, add_expense, read_expenses
from modules.analyzer import get_total_expenses, get_expenses_by_category, get_monthly_expenses, get_max_spend_day
from modules.budget_checker import set_budget, check_budget_status
from modules.visualizer import show_category_pie_chart, show_monthly_trend_chart
from modules.predictor import predict_next_month_expense

def menu():
    while True:
        print("\n==== Personal Finance Tracker ====")
        print("1. Add Expense")
        print("2. Show All Expenses")
        print("3. Show Expense Analysis")
        print("4. Set Monthly Budget")
        print("5. Check Budget Status")
        print("6. Show Charts")
        print("7. Predict Next Month’s Expense")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (Food, Rent, Travel, etc.): ")
            amount = input("Enter amount: ")
            try:
                amount = float(amount)
                add_expense(date, category, amount)
            except ValueError:
                print("❌ Please enter a valid amount.")

        elif choice == "2":
            expenses = read_expenses()
            if not expenses:
                print("No expenses found.")
            else:
                print("\n--- All Expenses ---")
                for e in expenses:
                    print(f"{e['Date']} - {e['Category']} - ₹{e['Amount']}")

        elif choice == "3":
            print("\n--- 📊 Expense Analysis ---")
            print(f"Total Expenses: ₹{get_total_expenses():.2f}")
            print("\nBy Category:")
            print(get_expenses_by_category())
            print("\nMonthly:")
            print(get_monthly_expenses())
            spend_day = get_max_spend_day()
            if spend_day:
                print(f"\n📅 Highest Spending Day: {spend_day.strftime('%Y-%m-%d')}")
            else:
                print("\n📅 Highest Spending Day: Not available yet.")

        elif choice == "4":
            amount = input("Enter your monthly budget: ")
            try:
                amount = float(amount)
                set_budget(amount)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "5":
            check_budget_status()

        elif choice == "6":
            print("\n--- Graph Options ---")
            print("1. Category-wise Pie Chart")
            print("2. Monthly Trend Line Chart")
            graph_choice = input("Choose chart type (1 or 2): ")

            if graph_choice == "1":
                show_category_pie_chart()
            elif graph_choice == "2":
                show_monthly_trend_chart()
            else:
                print("Invalid choice.")

        elif choice == "7":
            predict_next_month_expense()

        elif choice == "8":
            print("Goodbye! 💰")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    initialize_file()
    menu()

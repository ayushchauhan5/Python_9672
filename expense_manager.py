import pandas as pd
import matplotlib.pyplot as plt
import os

def load_expenses(expense):
    if os.path.exists(expense):
        return pd.read_csv(expense)
    else:
        print("File not found. Creating a new one.")
        return pd.DataFrame(columns=['Date', 'Category', 'Amount'])

def save_expenses(df, expense):
    df.to_csv(expense, index=False)

def add_expense(df, date, category, amount):
    new_expense = pd.DataFrame({'Date': [date], 'Category': [category], 'Amount': [amount]})
    df = pd.concat([df, new_expense], ignore_index=True)
    return df

def view_expenses(df):
    print("\n--- All Expenses ---")
    print(df)

def view_summary(df):
    print("\n--- Expense Summary ---")
    summary = df.groupby('Category')['Amount'].sum().reset_index()
    print(summary)
    plt.figure(figsize=(10, 6))
    plt.pie(summary['Amount'], labels=summary['Category'], autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Expense Summary by Category')
    plt.show()

def main():
    expense = "expenses.csv"
    expenses_df = load_expenses(expense)

    while True:
        print("\n--- Expense Manager ---")
        print("1. Add an Expense")
        print("2. View All Expenses")
        print("3. View Expense Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category: ")
            amount = float(input("Enter the amount: "))
            expenses_df = add_expense(expenses_df, date, category, amount)
            save_expenses(expenses_df, expense)
            print("Expense added successfully!")

        elif choice == "2":
            view_expenses(expenses_df)

        elif choice == "3":
            view_summary(expenses_df)

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
`

import sqlite3
import pandas as pd

DB_PATH = "db/expenses.db"

# -----------------------------
# Load Data
# -----------------------------
def load_data():
    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query("""
    SELECT t.tx_date, t.description, t.amount, c.name AS category
    FROM transactions t
    LEFT JOIN categories c ON t.category_id = c.id
    """, conn)

    conn.close()

    df["tx_date"] = pd.to_datetime(df["tx_date"])
    df["month"] = df["tx_date"].dt.to_period("M")

    return df

# -----------------------------
# Analysis
# -----------------------------
def analyze(df):
    # Income & Expense
    income = df[df["amount"] > 0]["amount"].sum()
    expense = -df[df["amount"] < 0]["amount"].sum()
    savings = income - expense

    print("\n📊 SUMMARY")
    print("Total Income:", income)
    print("Total Expense:", expense)
    print("Savings:", savings)

    # Category-wise
    print("\n📂 Category-wise Spending:")
    cat = -df[df["amount"] < 0].groupby("category")["amount"].sum()
    print(cat.sort_values(ascending=False))

    # Monthly trend
    print("\n📅 Monthly Spending:")
    monthly = -df[df["amount"] < 0].groupby("month")["amount"].sum()
    print(monthly)

# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":
    df = load_data()
    analyze(df)
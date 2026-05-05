import sqlite3
import pandas as pd
import os

DB_PATH = "db/expenses.db"

def export_report(month="2025-05"):
    os.makedirs("exports", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    # Fetch transactions
    df = pd.read_sql_query("""
    SELECT t.tx_date, t.description, t.amount, c.name AS category
    FROM transactions t
    LEFT JOIN categories c ON t.category_id = c.id
    """, conn)

    df["tx_date"] = pd.to_datetime(df["tx_date"])
    df["month"] = df["tx_date"].dt.to_period("M").astype(str)

    # Filter month
    df_month = df[df["month"] == month]

    # Category summary
    summary = -df_month[df_month["amount"] < 0].groupby("category")["amount"].sum()
    summary = summary.sort_values(ascending=False)

    file_path = f"exports/expense_report_{month}.xlsx"

    # Write Excel
    with pd.ExcelWriter(file_path) as writer:
        df_month.to_excel(writer, sheet_name="Transactions", index=False)
        summary.to_frame(name="Total Spend").to_excel(writer, sheet_name="Category Summary")

    conn.close()

    print(f"📄 Report exported: {file_path}")

# Run
if __name__ == "__main__":
    export_report("2025-05")
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

DB_PATH = "db/expenses.db"

# -----------------------------
# Load Data
# -----------------------------
def load_data():
    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query("""
    SELECT t.tx_date, t.amount, c.name AS category
    FROM transactions t
    LEFT JOIN categories c ON t.category_id = c.id
    """, conn)

    conn.close()

    df["tx_date"] = pd.to_datetime(df["tx_date"])
    df["month"] = df["tx_date"].dt.to_period("M")

    return df

# -----------------------------
# Create Charts
# -----------------------------
def create_plots(df):
    os.makedirs("outputs", exist_ok=True)

    # Category-wise bar chart
    cat = -df[df["amount"] < 0].groupby("category")["amount"].sum()
    cat = cat.sort_values(ascending=False)

    plt.figure()
    cat.plot(kind="bar")
    plt.title("Category-wise Spending")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/category_bar.png")
    plt.close()

    # Monthly line chart
    monthly = -df[df["amount"] < 0].groupby("month")["amount"].sum()

    plt.figure()
    monthly.plot(kind="line", marker="o")
    plt.title("Monthly Spending Trend")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig("outputs/monthly_line.png")
    plt.close()

    # Pie chart
    plt.figure()
    cat.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Spending Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("outputs/pie_chart.png")
    plt.close()

    print("📊 Charts saved in outputs/ folder")

# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":
    df = load_data()
    create_plots(df)
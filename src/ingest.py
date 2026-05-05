import pandas as pd
import sqlite3

DB_PATH = "db/expenses.db"

# -----------------------------
# 1. Read CSV
# -----------------------------
def read_csv(file_path):
    df = pd.read_csv(file_path)

    # Standardize columns
    df["tx_date"] = pd.to_datetime(df["Date"]).dt.date.astype(str)
    df["description"] = df["Description"].str.strip()
    df["amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df["account"] = df["Account"]

    # Keep required columns
    df = df[["tx_date", "description", "amount", "account"]]

    # Drop invalid rows
    df = df.dropna()

    return df

# -----------------------------
# 2. Insert into Database
# -----------------------------
def insert_data(df):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    for row in df.itertuples(index=False):
        cur.execute("""
            INSERT INTO transactions (tx_date, description, amount, account)
            VALUES (?, ?, ?, ?)
        """, (row.tx_date, row.description, row.amount, row.account))

    conn.commit()
    conn.close()

    print(f"✅ Inserted {len(df)} records into database")

# -----------------------------
# 3. Main Execution
# -----------------------------
if __name__ == "__main__":
    file_path = "data/expenses_sample.csv"

    df = read_csv(file_path)
    print("📊 Data Preview:")
    print(df.head())

    insert_data(df)
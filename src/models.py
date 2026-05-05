import sqlite3
import os

DB_PATH = "db/expenses.db"

def init_db():
    # Ensure db folder exists
    os.makedirs("db", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Enable foreign keys
    cur.execute("PRAGMA foreign_keys = ON;")

    # Create categories table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    );
    """)

    # Create transactions table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tx_date TEXT,
        description TEXT,
        amount REAL,
        account TEXT,
        category_id INTEGER,
        FOREIGN KEY(category_id) REFERENCES categories(id)
    );
    """)

    # Create budgets table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS budgets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        month TEXT,
        category_name TEXT,
        limit_amount REAL
    );
    """)

    conn.commit()
    conn.close()

    print("✅ Database & Tables Created Successfully!")

# Run directly
if __name__ == "__main__":
    init_db()
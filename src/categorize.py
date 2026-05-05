import sqlite3
import re
import pandas as pd

DB_PATH = "db/expenses.db"

# -----------------------------
# 1. Category Rules
# -----------------------------
RULES = {
    "Food": [r"swiggy", r"zomato", r"restaurant", r"cafe"],
    "Transport": [r"uber", r"ola", r"petrol", r"fuel"],
    "Shopping": [r"amazon", r"flipkart", r"myntra"],
    "Bills": [r"electricity", r"wifi", r"recharge"],
    "Entertainment": [r"netflix", r"spotify", r"movie"],
    "Income": [r"salary", r"credit"]
}

# -----------------------------
# 2. Classify Function
# -----------------------------
def classify(description, amount):
    desc = description.lower()

    # Income detection
    if amount > 0:
        return "Income"

    for category, patterns in RULES.items():
        for pattern in patterns:
            if re.search(pattern, desc):
                return category

    return "Uncategorized"

# -----------------------------
# 3. Main Function
# -----------------------------
def categorize_transactions():
    conn = sqlite3.connect(DB_PATH)

    # Load data
    df = pd.read_sql_query("SELECT * FROM transactions", conn)

    # Ensure categories table has entries
    categories = list(RULES.keys()) + ["Uncategorized"]
    for cat in categories:
        conn.execute("INSERT OR IGNORE INTO categories (name) VALUES (?)", (cat,))

    conn.commit()

    # Get category IDs
    cat_df = pd.read_sql_query("SELECT * FROM categories", conn)
    cat_map = dict(zip(cat_df["name"], cat_df["id"]))

    # Assign categories
    for row in df.itertuples():
        category = classify(row.description, row.amount)
        cat_id = cat_map[category]

        conn.execute("""
            UPDATE transactions
            SET category_id = ?
            WHERE id = ?
        """, (cat_id, row.id))

    conn.commit()
    conn.close()

    print("✅ Transactions categorized successfully!")

# -----------------------------
# Run file
# -----------------------------
if __name__ == "__main__":
    categorize_transactions()
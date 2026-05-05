import streamlit as st
import pandas as pd
import sqlite3

DB_PATH = "db/expenses.db"

st.set_page_config(page_title="Expense Tracker", layout="wide")

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
    df["month"] = df["tx_date"].dt.to_period("M").astype(str)

    return df

df = load_data()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🔍 Filters")

months = sorted(df["month"].unique())
selected_month = st.sidebar.selectbox("Select Month", months)

search = st.sidebar.text_input("🔎 Search Description")

df_filtered = df[df["month"] == selected_month]

if search:
    df_filtered = df_filtered[df_filtered["description"].str.contains(search, case=False)]

# -----------------------------
# Budget Input
# -----------------------------
st.sidebar.markdown("### 💰 Set Monthly Budget")
budget = st.sidebar.number_input("Enter Budget ₹", min_value=0, value=5000)

# -----------------------------
# Title
# -----------------------------
st.title("💰 Smart Expense Tracker")

# -----------------------------
# KPIs
# -----------------------------
income = df_filtered[df_filtered["amount"] > 0]["amount"].sum()
expense = -df_filtered[df_filtered["amount"] < 0]["amount"].sum()
savings = income - expense

col1, col2, col3 = st.columns(3)

col1.metric("💰 Income", f"₹{income:,.0f}")
col2.metric("💸 Expense", f"₹{expense:,.0f}")
col3.metric("📊 Savings", f"₹{savings:,.0f}")

# -----------------------------
# Budget Alert
# -----------------------------
if expense > budget:
    st.error(f"⚠️ You exceeded your budget by ₹{expense - budget:,.0f}")
else:
    st.success(f"✅ You are within budget. Remaining: ₹{budget - expense:,.0f}")

# -----------------------------
# Category Chart
# -----------------------------
st.subheader("📂 Category-wise Spending")
cat = -df_filtered[df_filtered["amount"] < 0].groupby("category")["amount"].sum()
st.bar_chart(cat)

# -----------------------------
# Daily Spending Trend
# -----------------------------
st.subheader("📅 Daily Spending Trend")
daily = -df_filtered[df_filtered["amount"] < 0].groupby("tx_date")["amount"].sum()
st.line_chart(daily)

# -----------------------------
# Top Insights
# -----------------------------
st.subheader("🔥 Insights")

if not cat.empty:
    top_category = cat.idxmax()
    st.write(f"💡 You spend most on **{top_category}**")

# -----------------------------
# Download Data
# -----------------------------
st.subheader("⬇️ Download Data")

csv = df_filtered.to_csv(index=False).encode("utf-8")
st.download_button("Download CSV", csv, "filtered_expenses.csv", "text/csv")

# -----------------------------
# Table
# -----------------------------
st.subheader("📋 Transactions")
st.dataframe(df_filtered.sort_values(by="tx_date", ascending=False), use_container_width=True)
# -----------------------------
# Expense Forecast
# -----------------------------
st.subheader("🔮 Expense Forecast")

monthly = -df[df["amount"] < 0].groupby("month")["amount"].sum()

if len(monthly) > 1:
    trend = monthly.diff().mean()
    predicted = monthly.iloc[-1] + trend
    st.info(f"📊 Predicted next month spending: ₹{predicted:,.0f}")
    # -----------------------------
# Subscription Detection
# -----------------------------
st.subheader("🔁 Detected Subscriptions")

subs = df_filtered["description"].value_counts()
subs = subs[subs > 1]

if not subs.empty:
    for name in subs.index:
        st.write(f"🔁 {name}")
else:
    st.write("No recurring subscriptions detected")
    # -----------------------------
# Category Budget Breakdown
# -----------------------------
st.subheader("📊 Category Budget Breakdown")

if not cat.empty:
    total = cat.sum()
    for category, value in cat.items():
        percent = (value / total) * 100
        st.write(f"{category}: ₹{value:,.0f} ({percent:.1f}%)")
        # -----------------------------
# Smart Insights
# -----------------------------
st.subheader("🧠 Smart Insights")

if not cat.empty:
    top_cat = cat.idxmax()
    percent = (cat.max() / cat.sum()) * 100

    st.write(f"💡 Highest spending is on **{top_cat}** ({percent:.1f}%)")

    if percent > 50:
        st.warning("⚠️ More than 50% of your spending is in one category!")
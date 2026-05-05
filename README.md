# 💰 Personal Expense Tracker (Go / Advanced Version)

## 🚀 Overview

This project is a **full-stack personal finance analytics system** built using Python.
It tracks expenses, stores them in a database, analyzes spending patterns, and provides an **interactive dashboard with smart insights and forecasting**.

Designed as an **industry-oriented project**, it demonstrates real-world data engineering, analytics, and dashboard development skills.

---

## 🎯 Problem Statement

Managing personal finances manually is inefficient and error-prone.
This project solves that by:

* Automating expense tracking
* Providing data-driven insights
* Helping users control spending and improve savings

---

## 🔥 Key Features

### 📥 Data Pipeline

* CSV ingestion (bank-like data)
* Data cleaning & transformation
* SQLite database storage

### 🧠 Smart Categorization

* Rule-based NLP classification
* Auto assignment of categories (Food, Transport, etc.)

### 📊 Analytics Engine

* Total income, expenses, savings
* Category-wise analysis
* Monthly trends
* Daily spending patterns

### 📈 Visualization

* Bar charts (category spending)
* Line charts (monthly trend)
* Pie charts (distribution)

### 💰 Budget System

* Monthly budget input
* Overspending alerts
* Remaining balance tracking

### 🔮 Advanced Features

* Expense forecasting (trend-based)
* Subscription detection (recurring payments)
* Smart insights (top spending, warnings)
* Category-wise budget breakdown

### 📤 Reporting

* Excel report generation
* CSV export (filtered data from dashboard)

### 🌐 Dashboard (Streamlit)

* Interactive UI
* Filters (month, category, search)
* KPI cards (Income, Expense, Savings)
* Real-time charts

---

## 🛠 Tech Stack

* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Database:** SQLite
* **Visualization:** Matplotlib
* **Dashboard:** Streamlit
* **ML (Optional Extension):** Scikit-learn

---

## 📁 Project Structure

```
expense-tracker/
├── data/            # Input CSV files
├── db/              # SQLite database
├── src/             # Core modules
│   ├── ingest.py
│   ├── categorize.py
│   ├── models.py
│   ├── analyze.py
│   ├── plots.py
│   ├── report.py
│   └── app_streamlit.py
├── outputs/         # Charts
├── exports/         # Reports
├── images/          # Screenshots
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd expense-tracker
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Project

### Step 1: Initialize Database

```bash
python src/models.py
```

### Step 2: Ingest Data

```bash
python src/ingest.py
```

### Step 3: Categorize Transactions

```bash
python src/categorize.py
```

### Step 4: Run Dashboard

```bash
streamlit run src/app_streamlit.py
```

---

## 📊 Sample Outputs

* Category-wise spending chart
* Monthly trend graph
* Budget alerts
* Forecast insights
* Excel report

(Add screenshots in `/images` folder)

---

## 🧠 Key Learnings

* Data cleaning and preprocessing
* Database design and management
* Data visualization techniques
* Dashboard development
* Financial analytics concepts
* End-to-end project structuring

---

## 💼 Industry Relevance

This project demonstrates skills required for:

* Data Analyst
* Python Developer
* Business Analyst
* Financial Analyst
* Data Engineer (beginner level)

---

## 🚀 Future Enhancements

* ML-based expense categorization
* Expense prediction using regression models
* Cloud deployment (Streamlit Cloud / AWS)
* Mobile app integration
* Multi-user authentication system

---

## 👩‍💻 Author

ARPITA BHENDIGERI

---

## ⭐ Support

If you found this project useful:

* ⭐ Star the repo
* 🔁 Share with others
* 💬 Give feedback

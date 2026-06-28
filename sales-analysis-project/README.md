# Online Retail Sales Analysis

## Project Overview

This project analyzes over 500,000 online retail transactions to identify sales trends, customer behavior, product performance, and international revenue using Python, SQL, and Tableau.

The project follows a complete analytics workflow from data cleaning to business recommendations and demonstrates the tools and techniques commonly used by data analysts.

---

## Getting Started

1. Download the Online Retail II dataset from the UCI Machine Learning Repository.
2. Place the dataset in the `Data/` folder.
3. Run `cleaning.py`.
4. Run `analysis.py`.
5. Import the cleaned CSV into MySQL.
6. Open the Tableau workbook.

## Dataset

The original dataset is not included in this repository because of GitHub's file size limits.

Dataset used:

Online Retail II Dataset (UCI Machine Learning Repository)

The cleaning script (`cleaning.py`) can be used to recreate the cleaned dataset.

## Business Problem

Management wants to better understand:

- Which products generate the most revenue?
- Who are the highest-value customers?
- How does revenue change over time?
- Which countries generate the most sales?
- What business opportunities exist for growth?

---

## Tools Used

- Python
- Pandas
- Matplotlib
- MySQL
- SQL
- Tableau Public
- Visual Studio Code

---

## Project Workflow

### 1. Data Cleaning (Python)

- Loaded the raw Excel dataset
- Removed missing customer IDs
- Removed invalid quantities and prices
- Created a Revenue column
- Converted dates to datetime format
- Exported a cleaned CSV for analysis

---

### 2. Exploratory Data Analysis (Python)

Analyzed:

- Top Products
- Monthly Revenue
- Top Customers

Created visualizations using Matplotlib.

---

### 3. SQL Analysis

Imported the cleaned data into MySQL and answered business questions using SQL.

Examples include:

- Top 10 Products
- Top Customers
- Monthly Revenue
- Revenue by Country
- Average Order Value

---

### 4. Tableau Dashboard

Created an interactive dashboard including:

- Total Revenue
- Total Orders
- Total Customers
- Monthly Revenue Trend
- Top Products
- Top Customers
- Revenue by Country (Excluding UK)
- Interactive Country Filter

---

## Key Findings

- Total revenue exceeded **$8.8 million**.
- More than **19,000 customer orders** were analyzed.
- Revenue peaked during **October and November**, indicating strong seasonal demand.
- Customer **18102** generated significantly more revenue than any other customer.
- International sales were strongest in **EIRE**, followed by the **Netherlands** and **Germany** (excluding the UK).

---

## Business Recommendations

- Improve customer retention efforts for high-value customers.
- Maintain sufficient inventory of the highest-performing products.
- Expand advertising and marketing efforts in international markets.
- Develop promotional campaigns during slower sales months to reduce seasonality.
- Expand advertising and marketing efforts in international markets.
- Maintain inventory levels for the highest-performing products.
---

## Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis
- SQL
- Data Visualization
- Dashboard Design
- Business Analysis
- Data Storytelling

---

## Dashboard Preview

![dashboard](Tableau/dashboard.png)
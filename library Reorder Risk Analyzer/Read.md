# 📚 Library Risk Record Analyzer

## 📌 Project Overview

The **Library Risk Record Analyzer** is a data analysis project built using Python, NumPy, pandas, and Matplotlib.

The goal of this project is to analyze library inventory and weekly borrowing records, identify inventory risks, understand borrowing demand, and provide data-driven restocking recommendations.

## 🎯 Project Objectives

- Inspect and understand library inventory data.
- Analyze weekly borrowing demand.
- Combine inventory and borrowing datasets.
- Calculate weeks of stock coverage.
- Classify books based on inventory risk using NumPy.
- Identify books requiring restocking.
- Perform statistical analysis.
- Visualize inventory and borrowing trends.
- Generate business insights and recommendations.

## 🛠️ Technologies Used

- **Python** – Programming language
- **NumPy** – Numerical operations and inventory classification
- **pandas** – Data cleaning, aggregation, merging, and analysis
- **Matplotlib** – Data visualization

## 📂 Dataset Files

The project uses two CSV files:

1. `Inventory.csv` – Contains library inventory information.
2. `weekly_loans.csv` – Contains weekly borrowing records.

## 📊 Project Tasks

### Task 01 – Data Inspection
- Inspect the first five rows.
- Check dataset shapes.
- Examine data types.

### Task 02 – Borrowing Demand Analysis
- Group borrowing records by `book_id`.
- Calculate total, average, and maximum loans.

### Task 03 – Dataset Merging
- Merge inventory and borrowing datasets.
- Handle missing borrowing values.

### Task 04 – Feature Engineering
- Calculate weeks of stock coverage.

### Task 05 – NumPy Classification
Classify books into five inventory risk categories:

- Out of stock
- No loan history
- Reorder now
- Monitor
- Healthy

### Task 06 – Data Sorting
- Sort books by borrowing demand.
- Identify the most and least borrowed books.
- Sort books by weeks of cover.

### Task 07 – Risk Analysis
- Count books in each risk category.
- Calculate risk percentages.
- Identify books with high demand and low stock.

### Task 08 – Statistical Analysis
- Calculate average stock.
- Identify books with the highest and lowest borrowing demand.
- Calculate median borrowing demand.
- Identify above-average borrowing demand.

### Task 09 – Business Insights
- Identify books requiring restocking.
- Find books with zero borrowing history.
- Analyze excessive inventory and low demand.
- Count healthy books.
- Recommend purchasing priorities.

### Task 10 – Data Visualization
Create visualizations using Matplotlib:
- Risk category bar chart.
- Top 10 most borrowed books.
- Inventory risk distribution pie chart.
- Current stock vs total loans scatter plot (planned).

## 💡 Key Skills Practiced

- DataFrame manipulation
- GroupBy and aggregation
- Dataset merging
- Boolean filtering
- NumPy array operations
- Statistical calculations
- Data sorting
- Feature engineering
- Data visualization
- Exploratory Data Analysis (EDA)
- Business-oriented data analysis

## 🚀 How to Run

1. Clone this repository.
2. Install the required libraries:

   `pip install numpy pandas matplotlib`

3. Place both CSV datasets in the project directory.
4. Run the Python notebook or script.

## 🎯 Learning Outcome

This project helped me practice NumPy and pandas through a practical data analysis scenario.

It demonstrates how raw inventory and borrowing records can be transformed into meaningful insights to support library inventory management and purchasing decisions.

---

**Project:** Library Risk Record Analyzer

**Focus:** NumPy | pandas | Matplotlib | Exploratory Data Analysis

**Status:** In Progress

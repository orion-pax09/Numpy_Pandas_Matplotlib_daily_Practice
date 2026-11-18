# Food Delivery Analytics: Order Time & Delivery Performance

An exploratory data analysis project focused on understanding food delivery operations, measuring delivery performance, and extracting meaningful insights from order data using Python.

## Project Overview

Food delivery data contains valuable information about order patterns, delivery efficiency, customer satisfaction, and business performance.

In this project, I explored a food delivery dataset to understand how orders perform across different cities, calculate delivery durations, categorize delivery speeds, and analyze customer ratings.

The project was developed using **Jupyter Notebook**, with Python libraries for data manipulation, numerical computation, and analysis.

## Objectives

- Explore and understand food delivery data.
- Clean and prepare data for analysis.
- Calculate delivery duration from order and delivery timestamps.
- Categorize deliveries based on their completion time.
- Analyze completed and cancelled orders.
- Compare delivery performance across cities.
- Examine customer ratings and order trends.

## Technologies & Libraries

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Jupyter Notebook | Interactive analysis environment |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations and conditional logic |
| Matplotlib | Data visualization |

## Dataset Description

The dataset contains food delivery order information, including:

| Column | Description |
|---|---|
| `order_id` | Unique order identifier |
| `order_time` | Time when the order was placed |
| `delivered_time` | Time when the order was delivered |
| `city` | Delivery city |
| `product` | Ordered food item |
| `price` | Order price |
| `status` | Order status |
| `rating` | Customer rating |

## Project Workflow

### 1. Data Loading & Exploration

- Imported Pandas, NumPy, and Matplotlib.
- Loaded the CSV dataset into a Pandas DataFrame.
- Explored the dataset using `head()`, `info()`, and `describe()`.
- Examined data types and missing values.

### 2. Data Cleaning

- Converted timestamp columns into datetime format.
- Handled missing delivery timestamps for cancelled orders.
- Prepared the dataset for accurate calculations and analysis.

### 3. Feature Engineering

Created additional features to extract more information from the dataset:

- **Delivery Minutes:** Calculated delivery duration using the difference between delivery and order timestamps.
- **Day Name:** Extracted the day of the week from delivery timestamps.
- **Delivery Category:** Classified deliveries into Fast, Normal, Slow, and Cancelled categories using NumPy conditional operations.

### 4. Data Analysis

Applied Pandas filtering, grouping, and aggregation techniques to investigate:

- Total orders per city.
- Completed orders per city.
- Average delivery time per city.
- Average customer ratings per city.
- Delivery performance across different categories.

### 5. Data Visualization

Used Matplotlib to explore and communicate patterns in the dataset through visualizations.

## Key Concepts Practiced

This project helped me gain practical experience with:

- NumPy arrays and conditional operations.
- Pandas Series and DataFrames.
- Data cleaning and missing value handling.
- Datetime conversion and time calculations.
- Feature engineering.
- Boolean indexing and filtering.
- `groupby()` and `agg()`.
- Lambda functions in grouped aggregation.
- Exploratory Data Analysis (EDA).
- Working with CSV files in Jupyter Notebook.

## Project Structure

```text
Food-Delivery-Analytics/
│
├── Food_Delivery_Analytics__Order_time_&_Delivery_Performance.ipynb
├── Food delivery analytics order time & delivery performance.csv
├── Requirement.txt
└── README.md
```

## How to Run

**1. Clone the repository**

```bash
git clone https://github.com/orion-pax09/Numpy_Pandas_Matplotlib_daily_Practice.git
```

**2. Navigate to the project directory**

```bash
cd "Numpy_Pandas_Matplotlib_daily_Practice/Food Delivery Analytics__Order time & Delivery Performance"
```

**3. Install dependencies**

```bash
pip install -r Requirement.txt
```

**4. Launch Jupyter Notebook**

```bash
jupyter notebook
```

Open the project notebook and execute the cells.

## What I Learned

Completing this project improved my understanding of how Python libraries can be used to work with real-world-style datasets.

I gained hands-on experience in cleaning data, handling missing values, working with datetime information, creating new features, and performing grouped analysis using Pandas and NumPy.

Most importantly, I learned how to approach a data analysis task step by step, from loading raw data to extracting useful information.

---

**Project Type:** Exploratory Data Analysis (EDA)  
**Environment:** Jupyter Notebook  
**Language:** Python

# 📊 Retail Sales Performance Analysis

A complete **Retail Sales Data Analysis and Business Intelligence project** using **Python, Pandas, NumPy, Matplotlib, Microsoft Excel, Jupyter Notebook, and Power BI**.

The project analyzes retail transactions to understand **sales, net sales, profit, products, customers, promotions, discounts, orders, and sales trends**.


## 📌 Project Overview

The objective of this project is to transform raw retail transaction data into meaningful business insights through **data cleaning, exploratory data analysis, visualization, data modeling, DAX, and interactive dashboards**.

### Key Areas

- Sales & Net Sales Analysis
- Profit & Profit Margin
- Product Performance
- Customer Analysis
- Promotion Performance
- Discount Analysis
- Monthly Sales Trends
- City-Level Sales
- Order & Unit Analysis
- Interactive Power BI Reporting

## 📁 Dataset

The project uses the following Excel workbook:

```text
data/store_data.xlsx
```
## Tables
```text
| Table         | Description               |
| ------------- | ------------------------- |
| Fact Table    | Retail sales transactions |
| Dim Customers | Customer information      |
| Dim Product   | Product information       |
| Dim Promotion | Promotion information     |
```
The dataset is used for educational and portfolio purposes.


## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Microsoft Excel
- Power BI
- DAX
- Git & GitHub

## 🔄 Project Workflow
```text
Excel Dataset
     ↓
Data Loading
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
Exploratory Data Analysis
     ↓
Python Visualization
     ↓
Power BI Data Modeling
     ↓
DAX Measures
     ↓
Interactive Dashboard
     ↓
Business Insights

## Python Analysis
```
Python is used for:

- Loading Excel data
- Data inspection
- Data cleaning
- Data type conversion
- Date feature creation
- Sales analysis
- Product analysis
- Customer analysis
- Promotion analysis
- Discount analysis
- Period comparison
- Data visualization

## Main Libraries
```text
pandas
numpy
matplotlib
openpyxl
jupyter
```
## 📏 Key DAX Measures
```text
Total Sales =
SUM('Fact Table'[Total Sales])

Net Sales =
SUM('Fact Table'[Net Sales])

Total Profit =
SUM('Fact Table'[Profit])

Total Units Sold =
SUM('Fact Table'[Units Sold])

Total Orders =
DISTINCTCOUNT('Fact Table'[Order ID])

Total Customers =
DISTINCTCOUNT('Fact Table'[CustomerID])

Total Discount =
SUM('Fact Table'[Discount])

Average Price Per Unit =
AVERAGE('Fact Table'[Price Per Unit])

Average Order Value =
DIVIDE([Net Sales], [Total Orders], 0)

Discount Rate =
DIVIDE([Total Discount], [Total Sales], 0)

Average Units Per Order =
DIVIDE([Total Units Sold], [Total Orders], 0)

Profit Margin =
DIVIDE([Total Profit], [Net Sales], 0)

Complete DAX documentation: powerbi/dax_measures.md
```
## 🔍 Business Questions
```text
This project is designed to answer:

1. What are the total sales and net sales?
2. What is the total profit and profit margin?
3. Which products generate the highest sales?
4. Which cities generate the highest sales?
5. How do sales change over time?
6. Which promotions perform better?
7. How much discount is provided?
8. How many orders and units are generated?
9. Which customers contribute the most sales?
10. How does sales performance change between different periods?
```
## 📂 Project Structure

```text
Retail-Sales-Performance-Analysis/
│
├── data/
│   └── store_data.xlsx
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── analysis.py
│   └── visualization.py
│
├── notebooks/
│   └── sales_analysis.ipynb
│
├── powerbi/
│   ├── Retail_Sales_Dashboard.pbix
│   └── dax_measures.md
│
├── screenshots/
│
├── README.md
├── requirements.txt
└── .gitignore

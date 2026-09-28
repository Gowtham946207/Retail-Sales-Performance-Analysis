# Power BI DAX Measures

This document contains the DAX measures used in the
Retail Sales Performance Analysis dashboard.

## Data Model

The Power BI model contains:

- Sheet3 — Sales transaction table
- Dim Customers — Customer information
- Dim Product — Product information
- Dim Promotion — Promotion information

The dimension tables are related to the sales transaction table
using their corresponding ID fields.

1. Total Sales
Total Sales =
SUM(Sheet3[Total Sales])


2. Net Sales
Net Sales =
SUM(Sheet3[Net Sales])


3. Total Units Sold
Total Units Sold =
SUM(Sheet3[Units Sold])


4. Total Transactions
Total Transactions =
COUNTROWS(Sheet3)


5. Total Customers
Total Customers =
DISTINCTCOUNT(Sheet3[CustomerID])

6. Total Discount
Total Discount =
SUM(Sheet3[Discount Value])


7. Average Price Per Unit
Average Price Per Unit =
AVERAGE(Sheet3[Price Per Unit])


8. Average Transaction Value
Average Transaction Value =
DIVIDE(
    [Net Sales],
    [Total Transactions],
    0
)


9. Discount Rate
Discount Rate =
DIVIDE(
    [Total Discount],
    [Total Sales],
    0
)


10. Average Units Per Transaction
Average Units Per Transaction =
DIVIDE(
    [Total Units Sold],
    [Total Transactions],
    0
)
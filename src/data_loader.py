"""
data_loader.py
--------------
Loads the retail sales Excel workbook into pandas DataFrames.
"""

from pathlib import Path
import pandas as pd


# Excel sheet names
FACT_SHEET = "Sheet3"
CUSTOMER_SHEET = "Dim Customers"
PRODUCT_SHEET = "Dim Product"
PROMOTION_SHEET = "Dim Promotion"


def load_data(filepath):
    """
    Load all required sheets from the Excel workbook.

    Returns:
        dict containing:
        - fact
        - customers
        - products
        - promotions
    """

    filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(
            f"Data file not found: {filepath}"
        )

    workbook = pd.ExcelFile(filepath)

    required_sheets = [
        FACT_SHEET,
        CUSTOMER_SHEET,
        PRODUCT_SHEET,
        PROMOTION_SHEET,
    ]

    missing_sheets = [
        sheet
        for sheet in required_sheets
        if sheet not in workbook.sheet_names
    ]

    if missing_sheets:
        raise ValueError(
            f"Missing sheet(s): {missing_sheets}\n"
            f"Available sheets: {workbook.sheet_names}"
        )

    fact = pd.read_excel(
        filepath,
        sheet_name=FACT_SHEET
    )

    customers = pd.read_excel(
        filepath,
        sheet_name=CUSTOMER_SHEET
    )

    products = pd.read_excel(
        filepath,
        sheet_name=PRODUCT_SHEET
    )

    promotions = pd.read_excel(
        filepath,
        sheet_name=PROMOTION_SHEET
    )

    return {
        "fact": fact,
        "customers": customers,
        "products": products,
        "promotions": promotions,
    }
"""
data_cleaning.py
----------------
Data cleaning functions for the Retail Sales Performance Analysis project.
"""

import pandas as pd


def clean_customers(customers: pd.DataFrame) -> pd.DataFrame:
    """
    Clean customer information.

    - Remove leading/trailing whitespace from City and State.
    - Handle missing text values.
    """

    customers = customers.copy()

    if "City" in customers.columns:
        customers["City"] = (
            customers["City"]
            .astype("string")
            .str.strip()
        )

    if "State" in customers.columns:
        customers["State"] = (
            customers["State"]
            .astype("string")
            .str.strip()
        )

    return customers


def clean_product(product: pd.DataFrame) -> pd.DataFrame:
    """
    Clean product information.

    - Remove unnecessary whitespace from product text fields.
    - Convert Price (INR) to numeric.
    """

    product = product.copy()

    for column in ["Product Line", "Product Name"]:
        if column in product.columns:
            product[column] = (
                product[column]
                .astype("string")
                .str.strip()
            )

    if "Price (INR)" in product.columns:
        product["Price (INR)"] = pd.to_numeric(
            product["Price (INR)"],
            errors="coerce"
        )

    return product


def clean_fact(fact: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the sales transaction table.

    - Convert Date to datetime.
    - Convert numeric sales fields to numeric values.
    - Remove leading/trailing whitespace from ID fields where applicable.
    """

    fact = fact.copy()

    # Date
    if "Date" in fact.columns:
        fact["Date"] = pd.to_datetime(
            fact["Date"],
            errors="coerce"
        )

    # Numeric columns
    numeric_columns = [
        "Discount Percentage",
        "Discount Value",
        "Net Sales",
        "Price Per Unit",
        "Total Sales",
        "Units Sold",
    ]

    for column in numeric_columns:
        if column in fact.columns:
            fact[column] = pd.to_numeric(
                fact[column],
                errors="coerce"
            )

    return fact


def clean_data(
    customers: pd.DataFrame,
    product: pd.DataFrame,
    fact: pd.DataFrame,
):
    """
    Run the cleaning process for all three tables.

    Returns:
        cleaned_customers,
        cleaned_product,
        cleaned_fact
    """

    customers = clean_customers(customers)
    product = clean_product(product)
    fact = clean_fact(fact)

    return customers, product, fact
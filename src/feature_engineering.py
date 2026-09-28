"""
feature_engineering.py
----------------------
Creates additional analytical features from the sales transaction data.
"""

import pandas as pd


def add_date_features(fact: pd.DataFrame) -> pd.DataFrame:
    """
    Add Year, Quarter, Month and Month Name to the sales data.
    """

    fact = fact.copy()

    fact["Date"] = pd.to_datetime(
        fact["Date"],
        errors="coerce"
    )

    fact["Year"] = fact["Date"].dt.year

    fact["Quarter"] = (
        "Q" + fact["Date"].dt.quarter.astype(str)
    )

    fact["Month"] = fact["Date"].dt.month

    fact["Month Name"] = fact["Date"].dt.strftime("%B")

    return fact


def add_sales_metrics(fact: pd.DataFrame) -> pd.DataFrame:
    """
    Add simple calculated metrics to the sales table.
    """

    fact = fact.copy()

    if "Total Sales" in fact.columns and "Discount Value" in fact.columns:
        fact["Discount Rate"] = (
            fact["Discount Value"]
            / fact["Total Sales"]
        ).fillna(0)

    if "Units Sold" in fact.columns:
        fact["Sales Per Unit"] = (
            fact["Net Sales"]
            / fact["Units Sold"]
        ).fillna(0)

    return fact


def create_features(fact: pd.DataFrame) -> pd.DataFrame:
    """
    Apply all feature engineering steps.
    """

    fact = add_date_features(fact)
    fact = add_sales_metrics(fact)

    return fact
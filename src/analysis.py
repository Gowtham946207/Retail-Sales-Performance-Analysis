"""
analysis.py
-----------
Sales analysis functions for the Retail Sales Performance Analysis project.

The functions work with the sales transaction table and return
pandas Series or DataFrames. Visualization is handled separately.
"""

import pandas as pd


# Q1 -----------------------------------------------------------------
def top_products(
    master: pd.DataFrame,
    n: int = 10,
) -> pd.Series:
    """Return the top products by Net Sales."""

    result = (
        master.groupby("Product ID")["Net Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    return result.head(n)


# Q2 -----------------------------------------------------------------
def monthly_sales(master: pd.DataFrame) -> pd.Series:
    """Return monthly Net Sales."""

    df = master.copy()
    df["Date"] = pd.to_datetime(df["Date"])

    result = (
        df.set_index("Date")["Net Sales"]
        .resample("ME")
        .sum()
    )

    return result


# Q3 -----------------------------------------------------------------
def sales_summary(master: pd.DataFrame) -> pd.Series:
    """Return the main sales KPIs."""

    return pd.Series(
        {
            "Total Sales": master["Total Sales"].sum(),
            "Net Sales": master["Net Sales"].sum(),
            "Total Units Sold": master["Units Sold"].sum(),
            "Total Discount": master["Discount Value"].sum(),
            "Total Transactions": len(master),
        }
    )


# Q4 -----------------------------------------------------------------
def discount_analysis(master: pd.DataFrame) -> pd.DataFrame:
    """Summarize discount performance."""

    result = (
        master.groupby("Product ID")
        .agg(
            Total_Sales=("Total Sales", "sum"),
            Total_Discount=("Discount Value", "sum"),
            Net_Sales=("Net Sales", "sum"),
            Units_Sold=("Units Sold", "sum"),
        )
        .sort_values("Net_Sales", ascending=False)
    )

    return result


# Q5 -----------------------------------------------------------------
def promotion_analysis(master: pd.DataFrame) -> pd.DataFrame:
    """Analyze sales and discounts by promotion."""

    result = (
        master.groupby("PromotionID")
        .agg(
            Total_Sales=("Total Sales", "sum"),
            Net_Sales=("Net Sales", "sum"),
            Total_Discount=("Discount Value", "sum"),
            Units_Sold=("Units Sold", "sum"),
        )
        .sort_values("Net_Sales", ascending=False)
    )

    return result


# Q6 -----------------------------------------------------------------
def customer_analysis(master: pd.DataFrame) -> pd.DataFrame:
    """Summarize sales performance by customer."""

    result = (
        master.groupby("CustomerID")
        .agg(
            Total_Sales=("Total Sales", "sum"),
            Net_Sales=("Net Sales", "sum"),
            Units_Sold=("Units Sold", "sum"),
            Transactions=("CustomerID", "size"),
        )
        .sort_values("Net_Sales", ascending=False)
    )

    return result


# Q7 -----------------------------------------------------------------
def compare_periods(
    master: pd.DataFrame,
    period1: tuple[str, str],
    period2: tuple[str, str],
) -> pd.DataFrame:
    """Compare sales performance between two date ranges."""

    df = master.copy()
    df["Date"] = pd.to_datetime(df["Date"])

    def summarize(start, end):
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)

        subset = df[
            (df["Date"] >= start)
            & (df["Date"] <= end)
        ]

        return pd.Series(
            {
                "Total Sales": subset["Total Sales"].sum(),
                "Net Sales": subset["Net Sales"].sum(),
                "Units Sold": subset["Units Sold"].sum(),
                "Discount": subset["Discount Value"].sum(),
                "Transactions": len(subset),
            }
        )

    first = summarize(*period1)
    second = summarize(*period2)

    result = pd.DataFrame(
        {
            "Period 1": first,
            "Period 2": second,
        }
    )

    result["Change %"] = (
        (result["Period 2"] - result["Period 1"])
        / result["Period 1"].replace(0, pd.NA)
        * 100
    ).round(2)

    return result


# Q8 -----------------------------------------------------------------
def filter_sales(
    master: pd.DataFrame,
    customer_id=None,
    product_id=None,
    promotion_id=None,
    date_range=None,
) -> pd.DataFrame:
    """Filter sales transactions using optional criteria."""

    df = master.copy()

    if customer_id is not None:
        df = df[df["CustomerID"] == customer_id]

    if product_id is not None:
        df = df[df["Product ID"] == product_id]

    if promotion_id is not None:
        df = df[df["PromotionID"] == promotion_id]

    if date_range is not None:
        df["Date"] = pd.to_datetime(df["Date"])

        start = pd.to_datetime(date_range[0])
        end = pd.to_datetime(date_range[1])

        df = df[
            (df["Date"] >= start)
            & (df["Date"] <= end)
        ]

    return df.reset_index(drop=True)
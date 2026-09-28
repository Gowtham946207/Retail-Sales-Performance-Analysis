"""
visualization.py
----------------
Visualization functions for the Retail Sales Performance Analysis project.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def save_figure(fig, filename: str):
    """Save a matplotlib figure to the outputs folder."""

    path = OUTPUT_DIR / filename
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return path


def plot_monthly_sales(monthly_sales: pd.Series):
    """Create a monthly Net Sales trend."""

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(
        monthly_sales.index,
        monthly_sales.values,
        marker="o",
    )

    ax.set_title("Monthly Net Sales Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Net Sales")

    ax.tick_params(axis="x", rotation=45)

    fig.tight_layout()

    save_figure(fig, "monthly_net_sales.png")

    return fig


def plot_top_products(top_products: pd.Series):
    """Create a bar chart of the top products."""

    fig, ax = plt.subplots(figsize=(10, 6))

    top_products.sort_values().plot(
        kind="barh",
        ax=ax,
    )

    ax.set_title("Top Products by Net Sales")
    ax.set_xlabel("Net Sales")
    ax.set_ylabel("Product")

    fig.tight_layout()

    save_figure(fig, "top_products.png")

    return fig


def plot_sales_by_city(sales_by_city: pd.Series):
    """Create a city-level sales comparison."""

    fig, ax = plt.subplots(figsize=(10, 6))

    sales_by_city.sort_values().plot(
        kind="barh",
        ax=ax,
    )

    ax.set_title("Net Sales by City")
    ax.set_xlabel("Net Sales")
    ax.set_ylabel("City")

    fig.tight_layout()

    save_figure(fig, "sales_by_city.png")

    return fig


def plot_promotion_performance(promotion_data: pd.DataFrame):
    """Visualize Net Sales by promotion."""

    data = promotion_data.sort_values(
        "Net_Sales",
        ascending=True,
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.barh(
        data.index.astype(str),
        data["Net_Sales"],
    )

    ax.set_title("Net Sales by Promotion")
    ax.set_xlabel("Net Sales")
    ax.set_ylabel("Promotion")

    fig.tight_layout()

    save_figure(fig, "promotion_performance.png")

    return fig


def plot_discount_analysis(discount_data: pd.DataFrame):
    """Visualize discount value by product."""

    data = discount_data.sort_values(
        "Total_Discount",
        ascending=True,
    ).tail(10)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.barh(
        data.index.astype(str),
        data["Total_Discount"],
    )

    ax.set_title("Top Products by Discount Value")
    ax.set_xlabel("Discount Value")
    ax.set_ylabel("Product")

    fig.tight_layout()

    save_figure(fig, "discount_analysis.png")

    return fig
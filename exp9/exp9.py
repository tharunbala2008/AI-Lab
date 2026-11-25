# Experiment 9: Data Visualization Using Matplotlib

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "experiment_9_retail_sales.csv"
if not csv_path.exists():
    from google.colab import files
    files.upload()
    csv_path = Path("experiment_9_retail_sales.csv")

# Read dataset
df = pd.read_csv(csv_path)

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Calculate revenue
df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]

print("----- RETAIL SALES DATASET -----")
print(df.head())

# Total sales analysis
print("\nTotal Units Sold:", df["Units_Sold"].sum())
print("Total Revenue: Rs.", df["Revenue"].sum())

# Monthly revenue analysis
monthly_sales = df.groupby(
    df["Date"].dt.to_period("M"))["Revenue"].sum()

print("\n----- MONTHLY REVENUE -----")
print(monthly_sales)

# Category-wise revenue
category_sales = df.groupby(
    "Category")["Revenue"].sum()

print("\n----- CATEGORY-WISE REVENUE -----")
print(category_sales)

# Region-wise revenue
region_sales = df.groupby(
    "Region")["Revenue"].sum()

print("\n----- REGION-WISE REVENUE -----")
print(region_sales)

# Visualization 1: Monthly Revenue Line Chart
plt.figure(figsize=(9, 5))
monthly_sales.index = monthly_sales.index.astype(str)
plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o",
    linewidth=2,
    label="Monthly Revenue")
plt.title("Monthly Retail Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (Rs.)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(base_dir / "monthly_revenue_line_chart.png", dpi=150)
plt.show()

# Visualization 2: Category-wise Bar Chart
plt.figure(figsize=(8, 5))
category_sales.plot(
    kind="bar",
    color="lightgreen",
    edgecolor="black")
plt.title("Category-wise Revenue Comparison")
plt.xlabel("Product Category")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(base_dir / "category_wise_revenue_bar_chart.png", dpi=150)
plt.show()

# Visualization 3: Region-wise Pie Chart
plt.figure(figsize=(7, 7))
plt.pie(
    region_sales,
    labels=region_sales.index,
    autopct="%1.1f%%",
    startangle=90)
plt.title("Region-wise Revenue Distribution")
plt.tight_layout()
plt.savefig(base_dir / "region_wise_revenue_pie_chart.png", dpi=150)
plt.show()

# Visualization 4: Units Sold vs Revenue
plt.figure(figsize=(8, 5))
plt.scatter(
    df["Units_Sold"],
    df["Revenue"],
    color="red",
    marker="o")
plt.title("Units Sold vs Revenue")
plt.xlabel("Units Sold")
plt.ylabel("Revenue (Rs.)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(base_dir / "units_sold_vs_revenue_scatter.png", dpi=150)
plt.show()

print("\nData Visualization Completed Successfully!")

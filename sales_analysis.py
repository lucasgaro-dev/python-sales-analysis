
import csv
import os
import matplotlib.pyplot as plt


def analyze_sales(filename):
    total_revenue = 0
    total_units = 0
    product_sales = {}
    product_units = {}

    with open(filename, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row = {
                key.strip(): value.strip()
                for key, value in row.items()
                if key is not None and value is not None
            }

            product = row["product"]
            quantity = int(row["quantity"])
            price = float(row["unit_price"])

            revenue = quantity * price
            total_revenue += revenue
            total_units += quantity

            product_sales[product] = (
                product_sales.get(product, 0) + revenue
            )

            product_units[product] = (
                product_units.get(product, 0) + quantity
            )

    print("SALES ANALYSIS REPORT")
    print("---------------------")
    print(f"Total revenue: ${total_revenue:.2f}")
    print(f"Total units sold: {total_units}")

    if not product_sales:
        print("No sales data available.")
        return

    best_product = max(product_sales, key=product_sales.get)
    print(f"Best-selling product by revenue: {best_product}")

    # Create folder for charts
    os.makedirs("charts", exist_ok=True)

    # Chart 1: Revenue by product
    plt.figure(figsize=(8, 5))
    plt.bar(product_sales.keys(), product_sales.values())
    plt.title("Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue ($)")
    plt.tight_layout()
    plt.savefig("charts/revenue_by_product.png")
    plt.close()

    # Chart 2: Units sold by product
    plt.figure(figsize=(8, 5))
    plt.pie(
        product_units.values(),
        labels=product_units.keys(),
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Distribution of Units Sold")
    plt.tight_layout()
    plt.savefig("charts/units_distribution.png")
    plt.close()

    print("\nCharts successfully generated in the charts folder.")


if __name__ == "__main__":
    analyze_sales("data/sales.csv")



import csv

def analyze_sales(filename):
    total_revenue = 0
    total_units = 0
    product_sales = {}

    with open(filename, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row = {
                key.strip(): value.strip()
                for key, value in row.items()
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

    print("SALES ANALYSIS REPORT")
    print("---------------------")
    print(f"Total revenue: ${total_revenue:.2f}")
    print(f"Total units sold: {total_units}")

    if product_sales:
        best_product = max(product_sales, key=product_sales.get)
        print(f"Best-selling product by revenue: {best_product}")
    else:
        print("No sales data available.")

if __name__ == "__main__":
    analyze_sales("data/sales.csv")


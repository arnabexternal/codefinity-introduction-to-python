# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for prod in products:
    product_details = products.get(prod)
    product_details[0] = float(product_details[0])
    product_details[1] = int(product_details[1])
    total_sales = product_details[0] * product_details[1]
    print(f"Total sales for {prod}: ${total_sales}")
    total_sales_list.append(total_sales)

total_sum = sum(total_sales_list)
print(f"Total sum of all sales: ${total_sum}")

min_sales = min(total_sales_list)
print(f"Minimum sales: ${min_sales}")

max_sales = max(total_sales_list)
print(f"Maximum sales: ${max_sales}")
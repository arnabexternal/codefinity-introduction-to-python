# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenue = []
    for item in range(len(prices)):
        revenue.append(prices[item] * quantities_sold[item])
    return revenue

def formatted_output(revenues):
    revenue_list = sorted(revenues)
    for revenue in revenue_list:
        print(f"{revenue[0]} has total revenue of ${revenue[1]}")



revenue_per_product = tuple(zip(products, calculate_revenue(prices, quantities_sold)))

formatted_output(revenue_per_product)

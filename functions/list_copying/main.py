# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

def apply_discount(prices):
    prices_copy = prices.copy()
    for price in range(len(prices_copy)):
        if prices_copy[price] > 2:
            prices_copy[price] -= discount_calculation(prices_copy[price])
    return prices_copy

def discount_calculation(amount):
    return amount * 10 / 100

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

print(f"Updated product prices: {updated_prices}")
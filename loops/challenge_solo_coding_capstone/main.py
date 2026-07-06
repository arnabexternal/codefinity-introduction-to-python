# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

for inv in inventory:
    stock_status = inventory.get(inv)
    if stock_status[0] < 30:
        print(f"{inv} need restocking. {inv} should be sold at the regular price of {stock_status[1]}.")
    elif stock_status[0] > 100:
        print(f"{inv} should be sold at the discounted price of {stock_status[2]}.")
    elif 30 < stock_status[0] < 100:
        print(f"{inv} should be sold at the regular price of {stock_status[1]}.")
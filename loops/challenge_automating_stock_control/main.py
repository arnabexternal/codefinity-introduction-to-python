# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print(f"Processing started")
for inv in inventory:
    print(f"Processing {inv}")
    stock_status = inventory.get(inv)
    while stock_status[0] < stock_status[1]:
        stock_status[0] += stock_status[2]
    if stock_status[0] > discount_threshold:
        stock_status[3] = True

print(f"Processing completed")
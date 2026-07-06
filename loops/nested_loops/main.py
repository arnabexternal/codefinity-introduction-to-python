produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce,dairy]

for groc in groceries:
    for gr in groc:
        print(f"Item name: {gr}")
        
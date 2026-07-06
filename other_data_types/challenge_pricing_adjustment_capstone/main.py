grocery_inventory = {
    "Milk":("Dairy",3.50,8),
    "Eggs":("Dairy",5.50,30),
    "Bread":("Bakery",2.99,15),
    "Apples":("Produce",1.50,50)
}

if (grocery_inventory.get("Eggs"))[1] > 5:
    grocery_inventory.update({"Eggs":("Dairy",4.50,30)})
    print(f"Eggs are too expensive, reducing the price by $1.")
else:
    print(f"The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes":("Produce",1.20,30)})
print(f"Inventory after adding Tomatoes:{grocery_inventory}")

milk_stock = grocery_inventory.get("Milk")[2]
if milk_stock < 10:
    milk_stock = milk_stock + 20
    grocery_inventory.update({"Milk":("Dairy",3.50,milk_stock)})
    print(f"Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print(f"Milk has sufficient stock.")

apple_price = (grocery_inventory.get("Apples"))[1]
if apple_price > 2:
    grocery_inventory.pop("Apples")
    print(f"Apples removed from inventory due to high price.")

print(f"Updated inventory:{grocery_inventory}")
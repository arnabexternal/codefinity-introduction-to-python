# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for indexNum in range(5):
    print(f"{weekdays[indexNum]}: Promotion on {daily_promotions[indexNum]}")
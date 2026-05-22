# Input variables
days_until_expiration = 5  # Example value
stock_level = 60  # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"

if product_type == "Perishable":
    if days_until_expiration <= 3 and stock_level > 50:
        print(f"30% discount applied")
    elif 4<= days_until_expiration <= 6 and stock_level > 50:
        print(f"20% discount applied")
    elif days_until_expiration > 6 and stock_level <= 50:
        print(f"10% discount applied")
elif not product_type == "Perishable":
    print(f"No discount available for non-perishable items.")
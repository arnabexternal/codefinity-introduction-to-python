def apply_discount(price, discount=0.05):
    price -= price * discount
    return price

def apply_tax(price, tax=0.07):
    price += price * tax
    return price

def calculate_total(price, discount=0.05, tax=0.07):
    total_discount = apply_discount(price, discount)
    total_tax = apply_tax(total_discount, tax)
    return total_tax

total_price_default = calculate_total(120)
print(f"Total cost with default discount and tax: ${total_price_default}")

total_price_custom = calculate_total(100, discount=0.10, tax=0.08)
print(f"Total cost with custom discount and tax: ${total_price_custom}")
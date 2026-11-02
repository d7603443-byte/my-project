# exercise 2

def add_to_total(total, price):
    return total + price
total = 0
total = add_to_total(total, 10)
total = add_to_total(total, 10)

print(total)

print(add_to_total(0, 10))
print(add_to_total(0, 10))

# exrecise 2
def apply_tax(prices, TAX):
    new_prices = []
    for i in prices:
        new_prices.append(i * TAX)
    return new_prices

prices = [100, 50]
with_tax = apply_tax(prices, 1.17)
print(prices)
print(with_tax)


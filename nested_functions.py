# exercise 1
def  format_receipt(items):
    def line(name, price):
        return name.ljust(10) + str(price)

    receipt = []

    for name, price in items:
        receipt.append(line(name, price))
    return "\n".join(receipt)

print(format_receipt([("Milk", 6), ("Bread", 9)]))

# exercise 2

def make_greeter(greeting):
    def greet(name):
        return greeting + ", " + name
    return greet

hello = make_greeter("Hello")
shalom = make_greeter("Shalom")
print(hello("Dana"))
print(shalom("Avi"))

# # exercise 3
def outer():
    message = "outer"

    def show():
        print("show:", message)
    def change():
        nonlocal message
        message = "changed"

    show()
    change()
    show()
outer()
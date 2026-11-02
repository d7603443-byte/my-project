# exercise 1
def make_greeting(name, greeting="Hello", punct="!"):
    return f"{greeting} {name}{punct}"
print(make_greeting("Dana"))
print(make_greeting("Avi", "good morning"))
print(make_greeting("Noa", punct="?"))

# exercise 2

def average(*average):
    return sum(average)/len(average)
    
print(average(80,90))
print(average(70,80,90,100))
try:
    average()
except ZeroDivisionError as error:
    print("error:", error)

# exercise 3
def format_profile(name, **details):
    return f"{name}{details}"

print(format_profile("Dana", age=24, city="Haifa"))
print(format_profile("Avi"))

# exercise 4
products = [("Laptop", 3500), ("Mouse", 80), ("Desk", 900)]

print(list(sorted(products, key=lambda p: p[1])))
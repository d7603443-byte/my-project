# exercise 1
def welcome(name):
    message = "Welcome " + name
    return message

message =  welcome("Dana")

print(welcome("Dana"))
print(message)

# exercise 2
x = "global"

def first():
    x = "local in first"
    print("1:", x)

def second():
    print("2:", x)

first()
second()
print("3:", x)

# exercise 3
count = 0
def add_one():
    result = count + 1
    print (result)

add_one()


# exercise 4
list_1 = [1, 2, 3]
numbers = list(range(5))
# exercise 1
def apply_to_all(numbers, action):
    result = []
    for n in numbers:
        result.append(action(n))
    return result

def double(n):
    return n * 2
    
print(apply_to_all([1,2,3], double))
print(apply_to_all([1,2,3],lambda n: n*n))
print(apply_to_all([1.6, 2.4], round))

# exercise 2
prices = [20, 75, 120, 45, 90]

with_fee = list(map(lambda p: p+10, prices))
cheap = list(filter(lambda p: p >100, prices))

print(with_fee)
print(cheap)

numbers = [25, 43, 64, 66, 3, 190]

sorted_num = list(sorted(map(lambda n: n, numbers)))
cheap_num = list(filter(lambda n: n <50, numbers))
print(sorted_num)
print(cheap_num)

# exercise 3
words = ["banana", "fig", "cherry", "kiwi"]

print(sorted(words, key=len))
print(max(words, key=len))

students = [("Dana", 92), ("David", 95), ("Noa", 84), ("Avi", 70)]

best = max(students, key=lambda s: s[1])

print(best)
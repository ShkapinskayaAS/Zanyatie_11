n = int(input())
d = {}

for i in range(n):
    name = input()
    price = int(input())
    quantity = int(input())
    d[name] = [price, quantity]

total = 0
most_expensive_name = ""
max_cost = -1

for name, data in d.items():
    price, quantity = data
    cost = price * quantity
    total = total + cost

    if cost > max_cost:
        max_cost = cost
        most_expensive_name = name

print(total)
print(most_expensive_name)

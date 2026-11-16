n = int(input())
d = {}

for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

keys = list(d)
best = keys[0]

for key in d:
    if d[key] > d[best]:
        best = key

print(best)

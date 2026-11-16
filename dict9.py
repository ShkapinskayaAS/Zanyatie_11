n = int(input())
d1 = {}

for i in range(n):
    key = input()
    value = int(input())
    d1[key] = value

m = int(input())
d2 = {}

for i in range(m):
    key = input()
    value = int(input())
    d2[key] = value

k = input()

d1.update(d2)

print(len(d1))
print(d1[k])

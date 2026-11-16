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

ignored = 0

for key, value in d2.items():
    if key not in d1:
        d1[key] = value
    else:
        ignored = ignored + 1

print(len(d1))
print(ignored)

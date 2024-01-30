a = int(input())
b = 0
c = min(1, a)
d = max(1, a) + 1
for i in range(c, d):
    b += i
print(b)
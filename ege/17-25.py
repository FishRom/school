b = 0
s = 0
for i in range(3672, 9117):
    if i % 3 == 2 and i % 5 == 4:
        b += 1
        s += i
print(b)
print(s)
        
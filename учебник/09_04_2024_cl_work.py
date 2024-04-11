import math
x = a
l = 0
while x < b:
    y1 = f(x)
    y2 = f(x + h)
    l =l + math.sqrt(h * h + (y1 - y2) * (y1 - y2))
    x += h
print(l)
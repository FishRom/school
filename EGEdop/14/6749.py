a = 2*729**1021-2*243**1022+81**1023-2*27**1024-1025
r = 0
while a > 0:
    if a % 3 == 0:
        r += 1
    a //= 3
print(r)
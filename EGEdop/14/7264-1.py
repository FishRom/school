a = 343**515 - 6*49**520 + 5*49**510 - 3*7**530 - 550
r = 0
while a > 0:
    if a % 7 == 6:
        r += 1
    a //= 7
print(r)
a = 243**540 - 6*9**530 + 21*3**511 - 3*3**70 - 200
r = 0
while a > 0:
    if a%9 == 8:
        r += 1
    a //= 9
print(r)

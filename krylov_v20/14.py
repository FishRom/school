a = 3**333 + 3**22 - 9**111 - 8
r = 0
while a > 0:
    if a % 3 == 2:
        r += 1
    a //= 3
print(r)
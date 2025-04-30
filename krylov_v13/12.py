n = '1' * 2022
while '11111' in n or '555' in n:
    if '11111' in n:
        n = n.replace('11111', '555', 1)
    else:
        n = n.replace('555', '5', 1)
print(n)
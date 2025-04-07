n = 2025*'1'
while '1111' in n or '5555' in n:
    if '1111' in n:
        n = n.replace('1111', '55', 1)
    else:
        n = n.replace('5555', '5', 1)

print(n)
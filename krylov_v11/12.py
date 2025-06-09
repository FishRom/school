n = '22' + '1'*2024 + '22'
while '2111' in n or '1112' in n:
    n = n.replace('111', '1', 1)
    if '21' in n:
        n = n.replace('21', '12', 1)
    else:
        n = n.replace('12', '1', 1)
print(n)
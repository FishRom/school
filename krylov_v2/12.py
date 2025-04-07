a = '1'*2026

while '11111' in a or '222' in a:
    if '11111' in a:
        a = a.replace('11111', '22', 1)
    else:
        a = a.replace('222', '2', 1)
print(a)
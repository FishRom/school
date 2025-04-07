a = '4'*50

while '444' in a or '333' in a:
    if '444' in a:
        a = a.replace('444', '3', 1)
    else:
        a = a.replace('333', '3344', 1)

    if '3443' in a:
        a = a.replace('3443', '0', 1)

print(sum([int(x) for x in a]))
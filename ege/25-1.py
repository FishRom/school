deli = []
for i in range(126849, 126872):
    for j in range(1, i + 1):
        if i % j == 0:
            deli.append(j)
            if len(deli) > 4:
                break
    if len(deli) == 4:
        print(*deli)

count = 0
maks = []
for i in range(1016, 7937):
    if i % 3 == 0 and (i // 7 != 0 and i // 17 != 0 and i // 19 != 0 and i // 27 != 0):
        count += 1
        maks.append(i)
print(count)
print(max(maks))
summ = 0
maks = 0
for i in range(2807, 8558 + 1):
    if bin(i)[-2:] == '11' and i % 9 == 5:
        summ += i
        maks = i
print(maks, summ)
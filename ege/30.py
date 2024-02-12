summ = 0
mini = []
for i in range(1529, 9482 + 1):
    if bin(i)[-2:] == '01' and i % 5 == 3:
        summ += i
        mini.append(i)
print(min(mini), summ)
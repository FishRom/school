from random import randint
a = []
for i in range(4):
    row = []
    for j in range(4):
        row.append(randint(10, 100))
    a.append(row)
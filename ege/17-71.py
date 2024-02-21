k = 0
mini = 99999999
for i in range(1031, 125889):
    if i % 10 != 5 and i ** 0.5 % 1 == 0:
        k += 1
        if i % 100 == 36:
            if mini > i:
                mini = i

print(k, mini)
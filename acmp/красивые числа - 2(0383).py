index = int(input())
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(10, 600000):
    d1 = int(len(str(i)))
    sum = (i // 100000) + (i // 10000) % 10 + (i // 1000) % 10 + (i // 100) % 10 + (i // 10) % 10 + (i % 10)
    if sum % d1 == 0:
        array.append(i)
print(array[index - 1])
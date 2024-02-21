count = 0
thirteenth_number = None
for num in range(2894, 174883):
    s = sum(map(int, str(num))) #находим сумму чисел
    if num % 10 == 8 and s > 22:
        count += 1
        if count == 13:
            thirteenth_number = num

print(count, thirteenth_number)
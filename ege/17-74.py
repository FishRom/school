closest_to_30000 = None
closest_difference = float('inf') #верхнее значение для сравнения
count = 0

for num in range(5903, 174204):
    if len(set(str(num))) == len(str(num)) and sum(1 for digit in str(num) if int(digit) > 4) == 3:
        count += 1
        difference = abs(num - 30000) #Всегда положительный результат за счет abs
        if difference < closest_difference:
            closest_difference = difference
            closest_to_30000 = num

print(count, closest_to_30000)

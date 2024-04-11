'''# Считываем количество групп избирателей
g = int(input())

# Считываем количество избирателей в каждой группе
group_sizes = list(map(int, input().split()))

# Сортируем группы по количеству избирателей
group_sizes.sort()

# Вычисляем минимальное количество сторонников партии
min_supporters = 0
for i in range(g // 2 + 1):
    min_supporters += (group_sizes[i] // 2) + 1

# Выводим минимальное количество сторонников партии
print(min_supporters)'''
print(385 % 24)
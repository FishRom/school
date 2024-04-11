# Считываем количество моментов времени
n = int(input())

# Создаем список для хранения моментов времени
moments = []

# Считываем моменты времени и добавляем их в список
for _ in range(n):
    h, m, s = map(int, input().split())
    moments.append((h, m, s))

# Сортируем моменты времени
moments.sort()

# Выводим отсортированные моменты времени
for moment in moments:
    print(moment[0], moment[1], moment[2])
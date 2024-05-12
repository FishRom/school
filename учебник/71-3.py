import math

# Функция для вычисления высоты объекта в зависимости от расстояния, начальной скорости и угла
def raschet_visot(distance, nach_v, angle):
    gravity = 9.8
    if nach_v == 0:
        time = 0
    else:
        time = distance / nach_v * math.cos(math.radians(angle))
    height = nach_v * time * math.sin(math.radians(angle)) - 0.5 * gravity * time ** 2
    return height

# Начальные условия
distance_start =0
distance_end = 10
step = 0.01
angles = [35.5, 65.8]
nach_v = 12

# Расчет длины кривой для каждого угла
for angle in angles:
    distance = distance_start
    curve_length = 0
    while distance < distance_end:
        height1 = raschet_visot(distance, nach_v, angle)
        height2 = raschet_visot(distance + step, nach_v, angle)
        curve_length += math.sqrt(step ** 2 + (height2 - height1) ** 2)
        distance += step
    print(f'Длина кривой при угле {angle}: {curve_length:.3f}')
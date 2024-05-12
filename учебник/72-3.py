import math


def cylinder_area(total_area):
    max_volume = 0
    best_r = 0
    best_h = 0

    for r in range(1, total_area):
        for h in range(1, math.floor(total_area - 2 * math.pi * r)):
            volume = math.pi * r**2 * h
            if volume > max_volume:
                max_volume = volume
                best_r = r
                best_h = h
    return best_r, best_h


total_area = 100
best_rad, best_hei = cylinder_area(total_area)

print(f"Радиус банки: {best_rad} см")
print(f"Высота банки: {best_hei} см")
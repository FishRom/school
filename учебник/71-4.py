from math import radians, cos, sin, sqrt


def poisk_visoti(x, skorost, alfa):
    g = 9.8
    if skorost == 0:
        t = 0
    else:
        t = x / skorost * cos(radians(alfa))
    return (skorost * t * sin(radians(alfa))) - ((g * t ** 2) / 2)


a = 0
rasstoyanie = 10
ygl = 35.5
nachalnaya_skorost = 12

for h in [0.00001, 0.0001, 0.001, 0.01, 0.1]:
    x = a
    L = 0
    while x < rasstoyanie:
        y1 = poisk_visoti(x, nachalnaya_skorost, ygl)
        y2 = poisk_visoti(x + h, nachalnaya_skorost, ygl)
        L += sqrt(h * h + (y2 - y1) * (y2 - y1))
        x += h
    print(f'Длина траектории для шага {h:.5f}: {L:.3f}')



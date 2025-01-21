import math

for i in range(2, 1000):
    colors = math.ceil(math.log2(i))
    v = (1280*960*colors)
    if (1392640*180)/v >= 24:
        print(i)
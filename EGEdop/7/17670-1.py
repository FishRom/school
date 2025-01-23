import math

for i in range(2, 1000):
    colors = math.ceil(math.log2(i))
    v_odnoy = math.ceil((1024*960)*colors)
    if (1474560*140)/v_odnoy >= 32:
        print(i)
import math

for i in range(1, 1000):
    a = math.ceil(math.log2(10+26+450))
    b = math.ceil((a*i)/8)
    c = (b*575/1024)
    print(c, i)
    if c > 100:
        break

#159 -> это i и это верный ответ. типо смотрим последнее число, оно было послежним в строках по выводу. чзх
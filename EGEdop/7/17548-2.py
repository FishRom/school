import math

colors = math.ceil(math.log2(2048)) #кол-во цветов
v = (1024*960)*colors #одна карточка
kolvo = (96468992*280)/v #(скорость*время)/объем
print(kolvo)
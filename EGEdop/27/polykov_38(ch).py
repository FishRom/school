from turtle import *

def f1(x, y):
    if y > 5.2 and x > 1:
        return 0
    elif (x > 2 and x < 6.8 and y > 2) or (6.8 < x < 10 and y > 0):
        return 1
    elif (x < 2 and y < 5.2) or (2 < x < 6.8 and y < 2):
        return 2
    else:
        return 3

with open('27-38b.txt', 'r') as f:
    f.readline()
    lenn = 3
    a = [[] for x in range(lenn)]
    zoom = 20.0, speed(50), tracer(80)
    up()
    for i in f:
        x, y = map(float, i.replace(',', '.').split())
        goto(x*20.0,y*20.0)
        if f1(x, y) == 0:
            dot(4, 'red')
        elif f1(x, y) == 1:
            dot(4, 'black')
        elif f1(x, y) == 2:
            dot(4, 'blue')
    done()
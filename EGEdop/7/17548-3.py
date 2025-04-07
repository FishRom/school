v = 1024*960*11
for x in range(1, 10000):
    if x * v > 96_468_992*280:
        break
    else:
        print(x)
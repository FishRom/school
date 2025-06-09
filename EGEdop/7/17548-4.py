v = 1024*960*11
print(96_468_992 * 280/v)
for z in range(1, 100000):
    if (96_468_992 * 280) > (v * z):
        print(z)
    else:
        break
v = (1024*960*13)
for i in range(1, 1000):
    if i * v > 1_474_560*280:
        break
    else:
        print(i)
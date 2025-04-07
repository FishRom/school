for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                v = c and (a or b) and (d <= b)
                if v:
                    #print(d, c, b, a)
                    print(b, c, a, d)
#bcad
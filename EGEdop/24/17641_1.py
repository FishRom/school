with open('24_17641.txt', 'r') as f:
    a = f.readline()
    print(a[:400])
    for i in range(6):
        a = a.replace('*+', '**').replace('+*', '**').replace('++', '**')
    for i in range(8, 1, -1):
        z = '*' * i
        a = a.replace(z, ' ')
    print(a[:200])
    b = [x for x in a.split(' ') if len(x) >= 142]
    #b = max([len(x) for x in a.split(' ') if eval(x) == 0])
    print(b)



#142

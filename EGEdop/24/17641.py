with open('24_17641.txt', 'r') as f:
    a = f.readline()
    print(a[:200])
    for i in range(6):
        a = a.replace('*+', '**').replace('+*', '**').replace('++', '**')
    print(a[:200])
    #a = a.replace('A*', 'A').replace('*A', 'A').replace('A+', 'A').replace('+A', 'A')
    print(a[:200])
    #a = a.split('A')
    #c = len([x for x in a if x == 0])
    #print(c)
    b = max([len(x) for x in a.split('A') if eval(x) == 0])
    #print(a[:200])
    print(b)
#142
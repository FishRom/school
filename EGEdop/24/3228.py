with open('24_3228.txt', 'r') as f:
    a = f.readline()
    print(a[:50])
    a = a.replace('AB', '+').replace('AC', '+')
    print(a[:100])
    a = a.replace('B', '-').replace('C', '-').replace('A', '-')
    print(a[:100])
    b = max([len(x) for x in a.split('-')])
print(b)
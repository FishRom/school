with open('24_3584.txt', 'r') as f:
    a = f.readline()
    print(a[:50])
    a = a.replace('BA', '+').replace('DA', '+')
    print(a[:100])
    a = a.replace('A', '-').replace('D', '-').replace('B', '-')
    print(a[:100])
    b = max([len(x) for x in a.split('-')])
print(b)
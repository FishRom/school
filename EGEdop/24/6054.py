with open('24_6054.txt', 'r') as f:
    a = f.readline()
    print(a[:100])
    a = a.replace('CCA', '+++').replace('BBA', '+++')
    print(a[:100])
    a = a.replace('B', '-').replace('C', '-').replace('A', '-')
    print(a[:100])
    b = max([len(x) for x in a.split('-')])
print(b)
with open('24_6029.txt', 'r') as f:
    a = f.readline()
    print(a[:100])
    a = a.replace('FE', '++').replace('EF', '++')
    print(a[:100])
    a = a.replace('E', '-').replace('F', '-').replace('D', '-')
    print(a[:100])
    b = max([len(x) for x in a.split('-')])
    print(b)
#11
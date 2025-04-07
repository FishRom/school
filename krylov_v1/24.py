with open('24var01.txt', 'r') as f:
    a = f.readline()
    print(a[:200])
    a = a.replace('+', '-')
    for i in '2345':
        a= a.replace(i, '1')
    for i in range(10, 1, -1):
        a = a.replace('-'+'0'*i + '1', '-01')
    a = a.replace('-01', '-0--1')
    for i in range(10, 2, -1):
        print('-'*i)
        a = a.replace('-'*i, '--')
    print(a[:200])

    b = [(len(x),x) for x in a.split('--')]
    b.sort()
    print(b[-3:])


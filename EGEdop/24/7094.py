'''with open('24_7094.txt', 'r') as f:
    a = f.readline()
    a = a.replace('U', 'A').replace('D', 'C').replace('F', 'C')
    a = a.replace('AA', 'A A').replace('AA', 'A A')
    a = a.replace('CC', 'C C').replace('CC', 'C C').replace(' A', ' ').replace('C ', ' ')
    b = max([len(x) for x in a.split()])
    print(b)'''

with open('24_7094.txt', 'r') as f:
    a = f.readline()
    a = a.replace('U', 'A').replace('D', 'C').replace('F', 'C')
    a = a.replace('CA', '+').replace('C', 'A')
    print(a[:50])
    b = max([len(x) for x in a.split('A')])
    print(b)
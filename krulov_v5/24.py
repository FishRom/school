with open('24var05.txt', 'r') as f:
    a = f.readline()
    a = a.replace('B', '-').replace('C', '-').replace('D', '-').replace('E', '-')
    a = a.replace('F', '-').replace('G', '-').replace('A', '+')
    print(a[:700])
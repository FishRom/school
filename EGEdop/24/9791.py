import string
with open('24_9791.txt', 'r') as f:
    a = f.readline()
    print(a[:50])
    z = '123456789' + string.ascii_uppercase
    print(z)
    for i in '123456789ABCDEF':
        a = a.replace(i, '+')
    for j in 'GHIJKLMNOPQRSTUVWXYZ':
        a = a.replace(j, '-')
    b = max([len(x) for x in a.split('-')])
print(b)
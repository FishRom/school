from ipaddress import *

for a in (0, 128, 192, 224, 240, 248, 252, 254, 255):
    f = True
    for i in ip_network(f'191.239.130.3/255.255.{a}.0', 0):
        v = f'{i:b}'
        if v[:16].count('1') < v[16:].count('1'):
            f = False
    if f:
        print(a)
        break
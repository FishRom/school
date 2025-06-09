from ipaddress import *

for a in range(1, 255):
    f = True
    for i in ip_network(f'126.255.{a}.100/255.255.240.0', 0):
        z = f'{i:b}'
        if z[:16].count('1') < z[16:].count('1'):
            f = False
    if f:
        print(a)
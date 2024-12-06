from ipaddress import *

net = ip_network('105.224.200.224/255.255.255.224', 0)

res = 0
for ip in net:
    if f'{ip:b}'.count('1') % 4 == 0:
        res += 1

print(res)
from ipaddress import *

net = ip_network('204.16.168.0/255.255.248.0', 0)
res = 0
for ip in net:
    if f'{ip:b}'.count('1') % 5 != 0:
        res += 1
print(res)
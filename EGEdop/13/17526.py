from ipaddress import *

net = ip_network('172.16.128.0/255.255.192.0', 0)

res = 0
for ip in net:
    if f'{ip:b}'.count('1') % 2 != 0:
        res += 1
print(res)
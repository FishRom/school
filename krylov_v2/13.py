from ipaddress import *

net = ip_network('200.33.100.0/255.255.248.0', 0)

res = 0
for ip in net:
    if f'{ip:b}'.count('1') % 7 != 0:
        res += 1
print(res)
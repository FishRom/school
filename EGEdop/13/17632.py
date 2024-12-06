from ipaddress import *

net = ip_network('112.160.0.0/255.240.0.0', 0)
res = 0
for ip in net:
    if f'{ip:b}'.count('1') % 5 == 0:
        res += 1
print(res)
#215766
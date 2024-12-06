from ipaddress import *

net = ip_network('115.192.0.0/255.192.0.0', 0)
res= 0

for ip in net:
    if f'{ip:b}'.count('1') % 3 != 0:
        res += 1
print(res)
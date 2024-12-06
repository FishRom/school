from ipaddress import *

net = ip_network('115.198.0.0/255.254.0.0', 0)

r = 0
for ip in net:
    if f'{ip:b}'.count('1') % 5 == 0:
        r += 1
print(r)
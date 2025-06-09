from ipaddress import *

net = ip_network('142.108.56.118/255.255.255.240', 0)

for ip in net:
    if f'{ip:b}':
        print(ip)
print(bin(142)[2:])
print(bin(108)[2:])
print(bin(56)[2:])
print(bin(127)[2:])
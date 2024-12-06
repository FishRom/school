from ipaddress import *

net = ip_network('192.168.32.48/255.255.255.240', 0)
res = 0
for ip in net:
    #print(ip, f'{ip:b}'.count('1') %2)
    if f'{ip:b}'.count('1') % 2 == 1:
        res += 1

print(res)
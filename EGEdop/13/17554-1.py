from ipaddress import *

net = ip_network('112.160.0.0/255.240.0.0', 0)
r = 0
for ip in net:
    if bin(int(ip))[2:].count('1') % 3 != 0:
        r += 1
print(r)
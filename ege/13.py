'''from ipaddress import *

net = ip_network('94.253.128.0/255.255.128.0', 0)

res = 0
for i in net:
    if f'{i:b}'.count('1') % 6 != 0 and f'{i:b}'[-3:] == '101':
        res += 1
print(res)'''


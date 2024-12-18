#199
'''from ipaddress import *

for A in range(256):
    net = ip_network(f'250.113.{A}.197/255.255.255.192', 0)
    if all(f'{ip:b}'[:16].count('0') <= f'{ip:b}'[16:].count('0') for ip in net):
        print(A)'''

#ответ- 192

#200

'''from ipaddress import *

for A in range(256):
    net = ip_network(f'196.233.{A}.52/255.255.255.248', 0)
    if all(f'{ip:b}'[:16].count('1') > f'{ip:b}'[16:].count('1') for ip in net):
        print(A)'''

#ответ - 192

#198
from ipaddress import *

for A in range(16,25):
    net = ip_network(f'243.46.4.198/{A}', 0)
    if all(f'{ip:b}'[:16].count('0') <= f'{ip:b}'[16:].count('0') for ip in net):   #параметр в маске
        print(net.netmask)
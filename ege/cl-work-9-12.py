#60

'''from ipaddress import *
for i in range(32):
    net = ip_network('145.192.186.230/' + str(i), 0)
    sub = str(net).split('/')
    if sub[0] == '145.192.160.0':
        print(net.netmask)'''

#70

'''from ipaddress import *
for i in range(31, -1, -1):
    net1 = ip_network('115.127.30.120/' + str(i), 0)
    net2 = ip_network('115.127.151.120/' + str(i), 0)
    sub1 = str(net1).split('/')
    sub2 = str(net2).split('/')
    if sub1[0] == sub2[0]:
        print(net1.netmask)
        break'''

#140

'''from ipaddress import *
for i in range(32):
    net1 = ip_network('112.166.78.114/' + str(i), 0)
    net2 = ip_network('112.166.78.117/' + str(i), 0)
    sub1 = str(net1).split('/')
    sub2 = str(net2).split('/')
    if sub1[0] != sub2[0]:
        print(net1.netmask) #ответ находится вот здесь
        print(str(net1).split('/')[1])'''

#194

'''from ipaddress import *
net = ip_network('186.135.80.0/255.255.252.0')
k=0

for ip in net:
    if f'{ip:b}'[:16].count('1') > f'{ip:b}'[16:].count('1'): #...для которых в двочиной записи адреса суммарное
        # кол-во единиц в левых 2-х байтах больше суммарного кол-ва единиц в правых двух байтах
        k += 1
print(k)'''


#195

from ipaddress import *
net = ip_network('117.157.2.8/255.255.A.0')
A = []
for i in range(1, 256):
    A.append(i)
k=0

for ip in net:
    if f'{ip:b}'[:16].count('1') <= f'{ip:b}'[16:].count('1'):
        k += 1
print(k)

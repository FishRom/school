from ipaddress import *
k = 0
for i in ip_network('116.29.170.89/255.255.255.224', 0):
    s = f'{i:b}'
    if s[:16].count('1') >= s[16:].count('1'):
        k += 1
print(k)
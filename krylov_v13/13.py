from ipaddress import *

for a in range(33):
    net = ip_network(f'252.63.194.3/255.255.{a}.0', 1)

from ipaddress import *

for mask in range(33):
	net = ip_network(f'84.32.84.32/{mask}', 0)
	#print(f'{net[-1]:b}', f'{net}')
	if f'{net[-2]:b}'.count('1') == 19:
		print(mask)
		break

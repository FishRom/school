from ipaddress import * 

res = []
for mask in range(33):
	net = ip_network(f'84.23.84.23/{mask}', 0)
	if net.network_address == ip_address('84.23.84.0'):
		byte = [int(x) for x in str(net.netmask).split('.')]
		res.append([sum(byte[2:]), net.netmask])
print(max(res))

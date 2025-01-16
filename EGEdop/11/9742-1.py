import math

alfabet = math.ceil(math.log2(1500 + 10)) #мощность алфавита
byte = math.ceil(105*alfabet/8) #сколько весит один индификатор
v = (byte * 16384)/2**10
print(v)
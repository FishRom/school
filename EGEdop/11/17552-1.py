import math

for i in range(1, 100):
    alfabet = math.ceil(math.log2(i))
    byte = math.ceil((261 * alfabet)/8)
    v = (252500 * byte)/2**20
    if v > 31:
        print(i)
        break

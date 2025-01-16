import math

for i in range(1, 700):
    alfabet = math.ceil(math.log2(10+52+458))
    byte = math.ceil(i*alfabet/8)
    v = (byte*862)/2**10
    if v <= 276:
        print(i)
    else:
        break

maks = 0
mini = []
q = 0
c = 0
w = 1
def sis(num, base):
    new = ''
    while num > 0:
        r = num % base
        new = new + str(r)
        num = num // base
    return int(new)

for i in range(1000, 9999 + 1):
    k = sis(i, 3)
    if len(str(k)) == 8 and i % 5 != 0 and i % 7 != 0 and i % 11 != 0:
        maks = i
        mini.append(i)
print(min(mini), maks)
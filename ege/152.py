f = open("17-1.txt", 'r')
flag = False
c = 0
pr = None
m = 100000
for i in f.readlines():
    i = int(i)
    if pr != None:
        if (convert(abs(i), 8) % 10 == 6 and i % 9 == 0) or (abs(pr) % 10 == 6 and pr % 3 == 0):
            c += 1
            if i < m:
                m = i
            if pr < m:
                m = pr
        pr = i
    else:
        pr = i
f.close()
print(c, m)
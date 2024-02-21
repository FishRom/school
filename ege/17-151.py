f = open("17-1.txt")
flag = False
c = 0
pr = None
m = 10001
for i in f.readlines():
    if pr != None:
        if abs(int(i)) % 10 == 6 and int(i) % 3 == 0 or (abs(pr) % 10 == 6 and pr % 3 == 0):
            c += 1
            if int(i) < m:
                m = int(i)
            if pr < m:
                m = pr
        pr = int(i)
    else:
        pr = int(i)
f.close()
print(c, m)
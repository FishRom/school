with open('24_9753.txt', 'r') as f:
    a = f.readline()
    res = 0
    #a = 'ASDYYFASFASYFSAFSYYADFDSASDFYASDFYSDFYYSDFYSDFYF'
    #print(a)
    a = [len(x) for x in a.split('Y')]
    for i in range(len(a) - 150):
        res = max(res, sum(a[i:i + 151]))
    print(a[:50])
    print(res)
    print(res + 150)
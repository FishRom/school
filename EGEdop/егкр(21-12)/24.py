with open('24_19254.txt', 'r') as f:     #FSRQ
    a = f.readline()
    print(a[:100])
    #a = 'HHHHHFSRQHHHFSRQHHHHHHHHFSRQHHHHHHHHHHHHHFSRQHHHHHHHH'
    a = [len(x) for x in a.split('FSRQ')]
    res = 0
    for i in range(len(a) - 80):
        res = max(res, sum(a[i:i+81]))
print(res + 4*80 + 6)
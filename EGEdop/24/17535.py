with open('24_17535.txt', 'r') as f:
    a = f.readline()
    print(a[:100])
    res = 0
    #a = 'DasfsadfCDsdfdsfdsfCDsfjhsjdfhkjdCDakjshfjdhfCDaskdjflkjCDasjhfkjsdhfkjdshCDasfsdfdsfCDskdjfldksjf'
    a = a.replace('CD', 'C D')
    b = [len(x) for x in a.split(' ')]
    for i in range(len(b) - 160):
        #print(b[i:i+161])
        res = max(sum(b[i:i+161]), res)
#print(b)
print(res)

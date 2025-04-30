with open('9_21704.csv', 'r') as f:
    for i in f:
        a = [int(x) for x in i.split(';')]
        z =1
        for v in range(1, len(a)):
            if a[v-1] <= a[v]:
                z = 0
                break
        if z == 0:
            continue
        if (a[0] + a[6])/2 >= sum(a[1:6])/5:
            print(sum(a))
            break
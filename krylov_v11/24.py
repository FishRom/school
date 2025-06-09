'''with open('24var11.txt', 'r') as f:
    a = f.readline()
    a = a.replace('AB', '+')
    s = []
    m = float('inf')
    for i in range(len(a)):
        if a[i] == '+':
            if len(s) < 20:
                s.append(i)
            else:
                m = min(i - s[0] + 1, m)
                s = s[1:] + [i]
print(m + 21)'''

with open('24var11.txt', 'r') as f:
    s = f.readline()
    z = 10**10
    #print(s[:20], s[-20:])
    a = [len(x) for x in s.split('AB')]
    for i in range(0, len(a) - 21):
        z = min(z, sum(a[i:i + 20]))
    print(z + 2 * 21)
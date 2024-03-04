def main():
    m = 500000
    k = 2
    f = [2, 3]
    i = 5
    p = 1

    while i < m:
        ass = True
        for j in range(k):
            if f[j] * f[j] > i:
                break
            if i % f[j] == 0:
                ass = False

        if ass:
            f.append(i)
            k += 1

        if i == p * 6 - 1:
            i = p * 6 + 1
            p += 1
        else:
            i = p * 6 - 1

    while True:
        s = map(int, input().split())
        b = s
        a = 0
        while b > 0:
            a += b % 10
            b = b // 10

        b = s
        b1 = b
        last = 0
        c = 0
        while b > 1:
            for z in range(len(f)):
                if z == len(f) - 1:
                    b = 1
                    break
                lastv = 0
                if b1 == f[z]:
                    b = 1
                    break
                while b % f[z] == 0:
                    v = f[z]
                    if v == last:
                        c += lastv
                    else:
                        while v > 0:
                            lastv += v % 10
                            v = v // 10
                        c += lastv

                    last = f[z]
                    b //= f[z]

            if a == c:
                print(1)
            else:
                print(0)
            c = 0

if __name__ == "__main__":
    main()

for a in range(50):
    for b in range(50):
        for c in range(50):
            n = '>'+'1'*a + '2'*b + '3'*c
            while '>1' in n or '>2' in n or '>3' in n:
                if '>1' in n:
                    n = n.replace('>1', '21>3', 1)
                if '>2' in n:
                    n = n.replace('>2', '32>', 1)
                if '>3' in n:
                    n = n.replace('>3', '11>2', 1)
            if n.count('1') == 71 and n.count('2') == 54 and n.count('3') == 37:
                print(b)
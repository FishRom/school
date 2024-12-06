#19

#21
'''def f(s, m):
    if s >= 25:
        return m % 2 == 0
    if m == 0:
        return 0
    if m % 2 == 0:
        return f(s+2, m-1) and f(s*2, m-1)
    else:
        return f(s+2, m-1) or f(s*2, m-1)


for k in range(1, 25):
    if not f(k, 2) and f(k, 4):
        print(k)
        '''

#20
'''def f(s, m):
    if s >= 25:
        return m % 2 == 0
    if m == 0:
        return 0
    if m % 2 == 0:
        return f(s+2, m-1) and f(s*2, m-1)
    else:
        return f(s+2, m-1) or f(s*2, m-1)


for k in range(1, 25):
    if not f(k, 1) and f(k, 3):
        print(k)'''

#c тремя кучками
#19

'''def f(x, y, p):
    if x+y >= 77 or p > 2:
        return p == 2
    return f(x+1, y, p+1) or f(x*2, y, p+1) or f(x, y+1, p+1) or f(x, y*2, p+1)
for s in range(1, 70):
    if f(7, s, 0) == True:
        print('#19', s)
        break'''

#20

'''def f(x, y, p):
    if x+y >= 77 or p > 3:
        return p == 3
    if p%2 == 0:
        return f(x+1, y, p+1) or f(x*2, y, p+1) or f(x, y+1, p+1) or f(x, y*2, p+1)
    else:
        return f(x+1, y, p+1) and f(x*2, y, p+1) and f(x, y+1, p+1) and f(x, y*2, p+1)
for s in range(1, 70):
    if f(7, s, 0) == True:
        print('#20', s)'''

#21

'''def f(x, y, p):
    if x+y >= 77 or p > 4:
        return p == 2 or p == 4
    if p%2 != 0:
        return f(x+1, y, p+1) or f(x*2, y, p+1) or f(x, y+1, p+1) or f(x, y*2, p+1)
    else:
        return f(x+1, y, p+1) and f(x*2, y, p+1) and f(x, y+1, p+1) and f(x, y*2, p+1)
for s in range(1, 70):
    if f(7, s, 0) == True:
        print('#21', s)
        break'''

'''///////////////////////////////////////////////////////////////////////////////////'''

#дз на 9.10.24

#2
def f(x, y, p):
    if x+y >= 83 or p > 2:
        return p == 2
    return f(x+1, y, p+1) or f(x*2, y, p+1) or f(x, y+1, p+1) or f(x, y*2, p+1)
for s in range(1, 74):
    if f(9, s, 0) == True:
        print('#19(2.1)', s)
        break

#2.2

def f(x, y, p):
    if x+y >= 83 or p > 3:
        return p == 3
    if p%2 == 0:
        return f(x+1, y, p+1) or f(x*2, y, p+1) or f(x, y+1, p+1) or f(x, y*2, p+1)
    else:
        return f(x+1, y, p+1) and f(x*2, y, p+1) and f(x, y+1, p+1) and f(x, y*2, p+1)
for s in range(1, 74):
    if f(9, s, 0) == True:
        print('#20(2.2)', s)

#2.3

def f(x, y, p):
    if x+y >= 83 or p > 4:
        return p == 2 or p == 4
    if p%2 != 0:
        return f(x+1, y, p+1) or f(x*2, y, p+1) or f(x, y+1, p+1) or f(x, y*2, p+1)
    else:
        return f(x+1, y, p+1) and f(x*2, y, p+1) and f(x, y+1, p+1) and f(x, y*2, p+1)
for s in range(1, 74):
    if f(9, s, 0) == True:
        print('#21(2.3)', s)
        break


#3

def f(x, y, p):
    if x+y >= 87 or p > 2:
        return p == 2
    return f(x+1, y, p+2) or f(x*2, y, p+1) or f(x, y+1, p+1) or f(x, y*2, p+1)
for s in range(0, 78):
    if f(9, s, 0) == True:
        print('#19(3.1)', s)
        break

#3.2

def f(x,y,p):
    if x+y >= 87 or p > 3:
        return p == 3
    if p%2 == 0:
        return f(x+1, y, p+1) or f(x*2, y, p+1) or f(x, y+1, p+1) or f(x, y*2, p+1)
    else:
        return f(x+1, y, p+1) and f(x*2, y, p+1) and f(x, y+1, p+1) and f(x, y*2, p+1)
for s in range(0, 78):
    if f(9, s, 0) == True:
        print('#20(3.2)', s)

#3.3

def f(x,y,p):
    if x+y >= 87 or p > 4:
        return p == 4 or p == 2
    if p%2 != 0:
        return f(x+1, y, p+1) or f(x*2, y, p+1) or f(x, y+1, p+1) or f(x, y*2, p+1)
    else:
        return f(x + 1, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 2, p + 1)
for s in range(1, 78):
    if f(9, s, 0) == True:
        print('#21(2.3)', s)
        break



#40

def f(s, m):
    if s >= 33:
        return m % 2 == 0
    if m == 0:
        return 0
    if m % 2 == 0:
        return f(s+3, m-1) and f(s*2, m-1)
    else:
        return f(s+3, m-1) or f(s*2, m-1)


for k in range(1, 33):
    if f(k, 2):
        print('#19(40.1)', k)
        break


#40.2
def f(s, m):
    if s >= 33:
        return m % 2 == 0
    if m == 0:
        return 0
    if m % 2 == 0:
        return f(s+3, m-1) and f(s*2, m-1)
    else:
        return f(s+3, m-1) or f(s*2, m-1)


for k in range(1, 33):
    if not(f(k, 1)) and f(k, 3):
        print('#20(40.2)', k)

#40.3
def f(s, m):
    if s >= 33:
        return m % 2 == 0
    if m == 0:
        return 0
    if m % 2 == 0:
        return f(s+3, m-1) and f(s*2, m-1)
    else:
        return f(s+3, m-1) or f(s*2, m-1)


for k in range(1, 33):
    if not(f(k, 2)) and f(k, 4):
        print('#21(40.3)', k)
        break
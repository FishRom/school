from math import sqrt
def isPrime( x ):
    if x <= 1:
        return False
    d = 2
    while d*d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

start = 55000000
end = 60000000

for i in range(start, end + 1):
  x = i
  while x % 2 == 0:
      x //= 2
  qX = round(sqrt(sqrt(x)))
  if isPrime(qX) and qX ** 4 == x:
    print(i, x)
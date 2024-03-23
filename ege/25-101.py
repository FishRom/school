'''def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


maks = []
start = 125697
end = 190234

count = 0
for num in range(start, end + 1):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and is_prime(i) and is_prime(num // i):
            maks.append(num)
            count += 1
print(count, max(maks))
'''

from math import sqrt

start, end = 125697, 190234

def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

count = 0
ma = 0
for i in range(start, end+1):
  for x in [2]+list(range(3,round(sqrt(i))+1,2)):
    if i % x == 0 and isPrime(x):
      y = i // x
      if x != y and isPrime(y):
        count += 1
        ma = i
        break

print( count, ma )


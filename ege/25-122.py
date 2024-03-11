'''from math import sqrt

start, end = 356712, 420901

def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

count = 0
s = 0
for i in range(start, end+1):
  q = round(sqrt(i))
  Dx = [2] + list( range(3, q+1, 2) )
  found = False
  for x in Dx:
    if i % x == 0 and isPrime(x):
      yz = i // x
      qyz = round(sqrt(yz))
      for y in range(x+1,qyz+1):
        if yz % y == 0 and isPrime(y) and (x % 10 == y % 10):
          z = yz // y
          found = True
          if z != y and z != x and isPrime(z) and (x % 10 == z % 10):
            count += 1
            s += i
          break
      if found: break

print( count, int(s/count) )'''

def is_prime(num):
    if num <= 1: return False
    d = 2
    while d * d <= num:
        if num % d == 0:
            return False
        d += 1
    return True

def find_divisors(num):
    divisors = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and is_prime(i):
            divisors.append(i)
            if is_prime(num // i):
                divisors.append(num // i)
                break
    return divisors

count = 0
total_sum = 0

for num in range(356712, 420902):
    divisors = find_divisors(num)
    if len(divisors) == 2 and divisors[0] % 10 == divisors[1] % 10:
        count += 1
        total_sum += num

if count > 0:
    average = total_sum // count
else:
    average = 0

print(count, average)


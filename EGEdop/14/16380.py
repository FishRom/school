a = 4*3125**2019 + 3*625**2020 - 2*125**2021 + 25**2022 - 4*5**2023 - 2024
r = 0
while a > 0:
    if a % 25 > 10:
        r += 1
    a //= 25
print(r)
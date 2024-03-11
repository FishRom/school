start = 1686
end = 13276
noDig = "02468"
f = True
s = 0
for x in range(start, end + 1):
    if all(c not in noDig for c in str(x)):
        s += sum(map(int, str(x)))
print(s)

a = input()
b = 0
c = 0
for i in range(len(a) - 2):
    if a[i] + a[i + 1] + a[i + 2] == "JOI":
        b += 1
    if a[i] + a[i + 1] + a[i + 2] == "IOI":
        c += 1
print(b)
print(c)

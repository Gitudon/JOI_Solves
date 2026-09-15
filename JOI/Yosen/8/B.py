a = [0] * 20
for i in range(20):
    a[i] = int(input())
b = []
for i in range(10):
    b.append(a[i])
c = []
for i in range(10, 20):
    c.append(a[i])
d = sorted(b)
e = sorted(c)
f = d[-1] + d[-2] + d[-3]
g = e[-1] + e[-2] + e[-3]
print(f, g)

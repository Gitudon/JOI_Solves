n = int(input())
m = int(input())
c = [0] * m
for i in range(m):
    c[i] = int(input())
a = []
for i in range(2 * n):
    a.append(i + 1)


def cut(a, k):
    b = a[k:] + a[:k]
    return b


def riful(a):
    b = []
    for i in range(n):
        b.append(a[i])
        b.append(a[n + i])
    return b


for i in range(m):
    if c[i] == 0:
        a = riful(a)
    else:
        a = cut(a, c[i])
for i in range(2 * n):
    print(a[i])

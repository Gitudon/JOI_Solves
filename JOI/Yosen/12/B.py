N = int(input())
a = [0] * N
b = [0] * N
c = [0] * N
for i in range(N):
    a[i], b[i], c[i] = map(int, input().split())
d = [0] * N
e = 0
for i in range(N):
    for j in range(N):
        if a[i] == a[j]:
            e += 1
    if e == 1:
        d[i] += a[i]
    e = 0
f = 0
for i in range(N):
    for j in range(N):
        if b[i] == b[j]:
            f += 1
    if f == 1:
        d[i] += b[i]
    f = 0
g = 0
for i in range(N):
    for j in range(N):
        if c[i] == c[j]:
            g += 1
    if g == 1:
        d[i] += c[i]
    g = 0
for i in range(N):
    print(d[i])

n, m = map(int, input().split())
a = [int(input()) for c in range(n)]
b = [int(input()) for b in range(m)]
d = [0] * n
for i in range(m):
    for j in range(n):
        if b[i] >= a[j]:
            d[j] += 1
            break
print(d.index(max(d)) + 1)

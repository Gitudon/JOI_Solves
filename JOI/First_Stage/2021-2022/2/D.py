N = int(input())
A = list(map(int, input().split()))
a = max(A)
b = []
for i in range(1, a + 1):
    c = 0
    for j in range(N):
        if A[j] == i:
            c += 1
    b.append(c)
d = 100
for i in range(len(b)):
    if b[i] != 0 and b[i] < d:
        d = b[i]
e = []
for i in range(len(b)):
    if b[i] == d:
        e.append(i + 1)
print(min(e))

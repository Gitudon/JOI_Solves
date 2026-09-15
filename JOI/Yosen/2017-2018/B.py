N = int(input())
A = list(map(int, input().split()))
c = 0
d = 1
for i in range(N):
    if A[i] == 1:
        d += 1
        if i == N - 1:
            if c < d:
                c = d
    else:
        if c < d:
            c = d
        d = 1
print(c)

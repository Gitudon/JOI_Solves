N, M = map(int, input().split())
A = [0] * M
B = [0] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())

for i in range(M):
    if A[i] >= N:
        A[i] = 0
    else:
        A[i] = N - A[i]
b = sorted(A)
ans = 0
for i in range(M - 1):
    ans += b[i]
print(ans)

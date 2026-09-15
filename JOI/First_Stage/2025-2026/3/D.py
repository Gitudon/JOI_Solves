N, M = map(int, input().split())

A = [0] * N
for i in range(N):
    A[i] = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans += max(A[i])
print(ans)

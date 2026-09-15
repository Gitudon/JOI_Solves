N, M = map(int, input().split())
A = list(map(int, input().split()))

B = [0] * (M + 1)
for i in range(N):
    B[A[i] - 1] += 1

ans = 0
for i in range(M + 1):
    if ans < B[i]:
        ans = B[i]

print(ans)

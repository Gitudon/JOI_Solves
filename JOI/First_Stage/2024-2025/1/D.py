N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(M):
        if A[i] > B[j]:
            ans += (A[i] + B[j]) * A[i]
        else:
            ans += (A[i] + B[j]) * B[j]
print(ans)

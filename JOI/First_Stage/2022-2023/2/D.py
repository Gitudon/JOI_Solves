N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans += A[i]
    for j in range(M):
        if ans == B[j]:
            ans = 0
print(ans)

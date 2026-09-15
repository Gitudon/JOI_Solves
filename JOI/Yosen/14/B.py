N = int(input())
M = int(input())
A = list(map(int, input().split()))
B = [[]] * M
for i in range(M):
    B[i] = list(map(int, input().split()))
ans = [0] * N

for i in range(M):
    a = 0
    for j in range(N):
        if B[i][j] == A[i]:
            ans[j] += 1
        else:
            a += 1
    ans[A[i] - 1] += a

for i in range(N):
    print(ans[i])

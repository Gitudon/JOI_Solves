N = int(input())
A = list(map(int, input().split()))

ans = 0
c_max = A[0]
for i in range(1, N * 2 + 2, 2):
    ans = max(ans, c_max + A[i])
    if i + 1 < N * 2 + 2:
        c_max = max(c_max, A[i + 1])
print(ans)

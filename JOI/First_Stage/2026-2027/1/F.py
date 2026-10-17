N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sabun = [B[i] - A[i] for i in range(N)]
sabun.sort(reverse=True)
ans = sum(A)

for i in range(N - X):
    ans += sabun[i]

for i in range(N - X, Y):
    if sabun[i] <= 0:
        break
    ans += sabun[i]

print(ans)

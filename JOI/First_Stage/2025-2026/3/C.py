N, X = map(int, input().split())
H = list(map(int, input().split()))

ans = 0
for i in range(N):
    if H[i] >= X:
        ans += 1

print(ans)

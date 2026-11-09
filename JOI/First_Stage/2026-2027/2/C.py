N, L, R = map(int, input().split())

ans = 0
for _ in range(N):
    H, S = map(str, input().split())
    H = int(H)
    if L <= H <= R and S == "Yes":
        ans += 1
print(ans)

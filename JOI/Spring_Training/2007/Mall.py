m, n = map(int, input().split())
a, b = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(n)]

# S: -1 を 0 とみなした値の累積和, B: -1 の個数の累積和
S = [[0] * (m + 1) for _ in range(n + 1)]
B = [[0] * (m + 1) for _ in range(n + 1)]
for y in range(n):
    for x in range(m):
        v = c[y][x]
        bad = 1 if v == -1 else 0
        S[y + 1][x + 1] = S[y][x + 1] + S[y + 1][x] - S[y][x] + (0 if bad else v)
        B[y + 1][x + 1] = B[y][x + 1] + B[y + 1][x] - B[y][x] + bad


def rect(T, x, y):
    # 左上 (x, y)、幅 a、高さ b の長方形の和
    return T[y + b][x + a] - T[y][x + a] - T[y + b][x] + T[y][x]


ans = 10**10
for i in range(m - a + 1):
    for j in range(n - b + 1):
        if rect(B, i, j) == 0:
            ans = min(ans, rect(S, i, j))
print(ans)

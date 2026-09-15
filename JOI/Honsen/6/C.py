n = int(input())
zahyo = set()
ans = 0
X = [0] * n
Y = [0] * n
for i in range(n):
    X[i], Y[i] = map(int, input().split())
    zahyo.add((X[i], Y[i]))

for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = X[i], Y[i]
        x2, y2 = X[j], Y[j]
        dx = x2 - x1
        dy = y2 - y1
        square = dx * dx + dy * dy
        x3 = x1 - dy
        y3 = y1 + dx
        x4 = x2 - dy
        y4 = y2 + dx
        if (x3, y3) in zahyo and (x4, y4) in zahyo:
            ans = max(ans, square)
        x3 = x1 + dy
        y3 = y1 - dx
        x4 = x2 + dy
        y4 = y2 - dx
        if (x3, y3) in zahyo and (x4, y4) in zahyo:
            ans = max(ans, square)
print(ans)

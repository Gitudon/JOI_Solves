N, M, D = map(int, input().split())
a = []
for i in range(N):
    a.append(input())
ans = 0
for i in range(N):
    length = 0
    for j in range(M):
        if a[i][j] == ".":
            length += 1
            if j == M - 1:
                ans += max(length + 1 - D, 0)
        elif a[i][j] == "#":
            ans += max(length + 1 - D, 0)
            length = 0
for j in range(M):
    length = 0
    for i in range(N):
        if a[i][j] == ".":
            length += 1
            if i == N - 1:
                ans += max(length + 1 - D, 0)
        elif a[i][j] == "#":
            ans += max(length + 1 - D, 0)
            length = 0
print(ans)

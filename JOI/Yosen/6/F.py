a, b = map(int, input().split())
n = int(input())
A = [[0] * b for i in range(a)]
for i in range(n):
    x, y = map(int, input().split())
    A[x - 1][y - 1] = 1
ans = 0


def route(i, j):
    global ans
    if i == a - 1 and j == b - 1:
        ans += 1
        return
    elif i > a - 1 or j > b - 1:
        return
    elif A[i][j] == 1:
        return
    route(i + 1, j)
    route(i, j + 1)


route(0, 0)
print(ans)

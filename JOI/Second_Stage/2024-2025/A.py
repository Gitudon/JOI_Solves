H, W, Q = map(int, input().split())

masked = [[False] * W for _ in range(H)]
color = [[0] * W for _ in range(H)]

for _ in range(Q):
    query = list(map(int, input().split()))
    qk = query[0]
    xk = query[1]
    yk = query[2]
    if qk == 1:
        ck = query[3]
        if not masked[xk - 1][yk - 1]:
            color[xk - 1][yk - 1] = ck
        if not masked[xk - 1][yk]:
            color[xk - 1][yk] = ck
        if not masked[xk][yk - 1]:
            color[xk][yk - 1] = ck
        if not masked[xk][yk]:
            color[xk][yk] = ck
    else:
        masked[xk - 1][yk - 1] = True
        masked[xk - 1][yk] = True
        masked[xk][yk - 1] = True
        masked[xk][yk] = True

for i in range(H):
    print(*color[i])

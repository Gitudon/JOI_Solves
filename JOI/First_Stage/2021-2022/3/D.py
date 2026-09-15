N, M = map(int, input().split())
X = [0] * M
Y = [0] * M
for i in range(M):
    X[i], Y[i] = map(int, input().split())
Z = [[]] * N
for i in range(N):
    Z[i] = [i + 1, i + 1]
for j in range(M):
    for i in range(N):
        if Z[i][0] == X[j]:
            Z[i][1] = Y[j]
for i in range(N):
    print(Z[i][1])

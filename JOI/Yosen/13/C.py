W, H, N = map(int, input().split())
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
ans = 0
for i in range(N - 1):
    distx = abs(X[i + 1] - X[i])
    disty = abs(Y[i + 1] - Y[i])
    if (X[i + 1] > X[i] and Y[i + 1] > Y[i]) or ((X[i + 1] < X[i] and Y[i + 1] < Y[i])):
        ans += max(distx, disty)
    elif (X[i + 1] >= X[i] and Y[i + 1] <= Y[i]) or (
        (X[i + 1] <= X[i] and Y[i + 1] >= Y[i])
    ):
        ans += distx + disty
print(ans)

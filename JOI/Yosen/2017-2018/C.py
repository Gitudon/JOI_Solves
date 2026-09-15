H, W = map(int, input().split())
A = [0] * H
one = 0
two = 0
for i in range(H):
    A[i] = list(map(int, input().split()))
cost = []
for h in range(H):
    for w in range(W):
        c = 0
        for i in range(H):
            for j in range(W):
                c += min(abs(i - h) * A[i][j], abs(j - w) * A[i][j])
        cost.append(c)
print(min(cost))

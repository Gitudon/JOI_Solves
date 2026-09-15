N = int(input())
X = list(map(int, input().split()))
M = int(input())
A = list(map(int, input().split()))
for j in range(M):
    if X[A[j] - 1] + 1 not in X:
        if X[A[j] - 1] != 2019:
            X[A[j] - 1] += 1
for i in range(N):
    print(X[i])

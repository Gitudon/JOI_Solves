N, M = map(int, input().split())
A = [0] * N
for i in range(N):
    A[i] = int(input())
for k in range(1, M + 1):
    for i in range(N):
        if 0 <= i <= N - 2:
            if A[i] % k > A[i + 1] % k:
                a = A[i]
                A[i] = A[i + 1]
                A[i + 1] = a
for i in range(N):
    print(A[i])

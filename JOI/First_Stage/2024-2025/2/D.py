N = int(input())
A = list(map(int, input().split()))

for j in range(N - 1):
    k = len(A)
    tmp = [0] * (k - 1)
    for i in range(k - 1):
        tmp[i] = A[i] + A[i + 1]
    print(*tmp)
    A = tmp

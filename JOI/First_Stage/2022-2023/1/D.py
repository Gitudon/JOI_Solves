N = int(input())
A = list(map(int, input().split()))

a = []
for i in range(N):
    a.append(0)
for i in range(2 * N - 1):
    for j in range(N):
        if A[i] == j + 1:
            a[j] += 1
for i in range(N):
    if a[i] == 1:
        print(i + 1)

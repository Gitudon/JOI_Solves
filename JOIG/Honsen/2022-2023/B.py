N = int(input())
A = list(map(int, input().split()))
for i in range(N - 1):
    b = []
    for j in range(len(A) - 1):
        b.append(abs(A[j] - A[j + 1]))
    A = b
print(*b)

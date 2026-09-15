N = int(input())
A = list(map(int, input().split()))
a = max(A)
b = min(A)
for i in range(N):
    print(max(abs(A[i] - a), abs(A[i] - b)))

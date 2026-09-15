N = int(input())
A = list(map(int, input().split()))
left = [0] * (N + 1)
right = [0] * (N + 1)
for i in range(N):
    left[i + 1] = left[i] + (A[i] == 0)
    right[i + 1] = right[i] + (A[N - i - 1] == 1)
res = N
for i in range(N + 1):
    res = min(res, left[i] + right[N - i])
print(res)

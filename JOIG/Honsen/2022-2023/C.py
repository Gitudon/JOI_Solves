import bisect


def lower_bound(arr, x):
    index = bisect.bisect_left(arr, x)
    return index


N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def calc(x):
    i = lower_bound(A, x)
    res = 0
    if i - 1 >= 0:
        res = max(res, K - abs(x - A[i - 1]))
    if i < N:
        res = max(res, K - abs(x - A[i]))
    return res


for i in range(M):
    print(calc(B[i]))

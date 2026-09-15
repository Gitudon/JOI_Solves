N = int(input())
A = list(map(int, input().split()))

A = sorted(A, reverse=True)
singaku = 10**8
ans = -1
for i in range(N - 1):
    if A[i] != A[i + 1]:
        singaku_dash = abs(N - 2 * (i + 1))
        if singaku_dash < singaku:
            ans = A[i]
            singaku = singaku_dash
print(ans)

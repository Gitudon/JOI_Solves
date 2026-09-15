N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

gusu = []
kisu = []

for i in range(N):
    if A[i] % 2 == 0:
        gusu.append(A[i])
    else:
        kisu.append(A[i])

gusu.sort(reverse=True)
kisu.sort(reverse=True)

if len(gusu) >= K:
    ans = max(ans, sum(gusu[:K]))

if len(kisu) >= K:
    ans = max(ans, sum(kisu[:K]))

print(ans)

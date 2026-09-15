N = int(input())
C = list(map(int, input().split()))

for i in range(N):
    ans = 0
    for j in range(N):
        if C[i] == C[j]:
            ans += abs(i - j)
    print(ans)

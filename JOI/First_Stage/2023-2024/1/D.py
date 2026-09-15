N = int(input())
A = list(map(int, input().split()))
ans = [False] * 10
for i in range(N):
    ans[A[i]] = True
for i in range(10):
    if ans[i]:
        print(i)

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = []
if N >= M:
    for i in range(M):
        if B[i] in A:
            ans.append(B[i])
else:
    for i in range(N):
        if A[i] in B:
            ans.append(A[i])
ans = sorted(ans)
done = []
for i in range(len(ans)):
    if ans[i] not in done:
        print(ans[i])
        done.append(ans[i])

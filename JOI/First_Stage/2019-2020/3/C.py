N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    buf = 1
    now = A[i]
    for j in range(i + 1, N):
        if now <= A[j]:
            buf += 1
            now = A[j]
        else:
            break
    ans = max(buf, ans)
print(ans)

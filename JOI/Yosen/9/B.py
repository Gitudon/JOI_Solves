N, M = map(int, input().split())
a = [0] * N
b = [0] * M
for i in range(N):
    a[i] = int(input())
for i in range(M):
    b[i] = int(input())
ans = 0
current = 1
for i in range(M):
    ans += 1
    current += b[i]
    if current >= N:
        print(ans)
        exit()
    if a[current - 1] > 0:
        current += a[current - 1]
    elif a[current - 1] < 0:
        current -= abs(a[current - 1])
        if current <= 0:
            current = 1
    if current >= N:
        print(ans)
        exit()

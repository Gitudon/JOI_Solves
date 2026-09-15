n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
ans = [0] * n
c = 1
while s != [-1] * n:
    d = 0
    t = max(s)
    for i in range(n):
        if s[i] == t:
            ans[i] = c
            d += 1
            s[i] = -1
    c += d
for i in range(n):
    print(ans[i])

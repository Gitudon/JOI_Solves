n, k = map(int, input().split())
cards = [int(input()) for _ in range(k)]
ans = []
numbers = [0] * n
for c in cards:
    if c != 0:
        numbers[c - 1] = 1
kukan = []
buf = []
for i in range(n):
    if numbers[i] == 1:
        if len(buf) == 0:
            buf.append(i + 1)
    else:
        if len(buf) == 1:
            buf.append(i)
            kukan.append(buf)
            buf = []
if len(buf) == 1:
    buf.append(n)
    kukan.append(buf)
for k in kukan:
    ans.append(k[1] - k[0] + 1)

if 0 in cards:
    for k in kukan:
        ans.append(k[1] - k[0] + 2)
    for i in range(len(kukan) - 1):
        if kukan[i][1] + 2 == kukan[i + 1][0]:
            ans.append(kukan[i + 1][1] - kukan[i][0] + 1)

print(max(ans))

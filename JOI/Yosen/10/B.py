a = input()
N = int(input())
ans = 0
for i in range(N):
    b = input()
    c = b + b + b
    if a in c:
        ans += 1
print(ans)

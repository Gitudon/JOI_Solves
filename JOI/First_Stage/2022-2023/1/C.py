N = int(input())
S = input()

x = 1
ans = 0
for i in range(N):
    if S[i] == "L":
        if x == 1:
            x = 1
        else:
            x -= 1
    else:
        if x == 3:
            x = 3
        else:
            x += 1
    if x == 3:
        ans += 1
print(ans)

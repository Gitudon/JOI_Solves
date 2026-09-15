N = int(input())
S = input()
ans = 0
for i in range(N):
    if S[i] == "j" or S[i] == "i":
        ans += 2
    else:
        ans += 1
print(ans)

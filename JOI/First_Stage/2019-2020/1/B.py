N = int(input())
S = input()
ans = 0
a = ["a", "i", "u", "e", "o"]
for i in range(N):
    if S[i] in a:
        ans += 1
print(ans)

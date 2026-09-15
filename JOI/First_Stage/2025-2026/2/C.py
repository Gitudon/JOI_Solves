N = int(input())
S = input()

ans = 0
for i in range(N - 2):
    buf = S[i] + S[i + 1] + S[i + 2]
    if buf == "AOI" or buf == "IOI":
        ans += 1

print(ans)

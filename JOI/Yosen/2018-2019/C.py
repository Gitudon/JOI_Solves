N = int(input())
S = input()
i = 0
ans = 0
while i < N - 1:
    if S[i] == "O":
        if S[i + 1] == "X":
            ans += 1
            i += 2
        else:
            i += 1
    else:
        if S[i + 1] == "O":
            ans += 1
            i += 2
        else:
            i += 1
print(ans)

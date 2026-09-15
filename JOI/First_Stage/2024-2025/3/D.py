N = int(input())
S = input()

ans = "No"
for i in range(N // 2):
    T = S[: i + 1]
    m = N // (i + 1)
    string = ""
    for j in range(m):
        string += T
    if string == S:
        ans = "Yes"
print(ans)

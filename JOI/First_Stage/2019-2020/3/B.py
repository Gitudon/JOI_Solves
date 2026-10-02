N = int(input())
S = input()
li = [0] * N
for i in range(N):
    li[i] = S[i]
for i in range(N - 2):
    if li[i] == "j" and li[i + 1] == "o" and li[i + 2] == "i":
        li[i] = "J"
        li[i + 1] = "O"
        li[i + 2] = "I"
ans = ""
for i in range(N):
    ans += li[i]
print(ans)

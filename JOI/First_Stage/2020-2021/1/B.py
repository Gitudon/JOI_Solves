N = int(input())
S = input()

ans = ""
for i in range(N):
    if ord(S[i]) == 74:
        ans += "J"
for i in range(N):
    if ord(S[i]) == 79:
        ans += "O"
for i in range(N):
    if ord(S[i]) == 73:
        ans += "I"
print(ans)

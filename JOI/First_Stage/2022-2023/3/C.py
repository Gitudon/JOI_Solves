N = int(input())
S = input()
T = [0] * N
for i in range(N):
    T[i] = S[i]
for i in range(N - 1):
    if T[i] == T[i + 1]:
        T[i] = chr(ord(T[i]) - 32)
        T[i + 1] = chr(ord(T[i + 1]) - 32)
ans = ""
for i in range(N):
    ans += T[i]
print(ans)

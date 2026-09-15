N = int(input())
S = input()

c = 0
for i in range(1, N + 1):
    if i % 2 == 1:
        if S[i - 1] != "I":
            c += 1
    else:
        if S[i - 1] != "O":
            c += 1
print(c)

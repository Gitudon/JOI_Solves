N = int(input())
K = int(input())
S = input()

c = 0
for i in range(N - 1):
    if S[i] == "R":
        c += 1
if c != K:
    print("R")
else:
    print("W")

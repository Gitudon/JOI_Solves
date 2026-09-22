Q = int(input())
S = []
for i in range(Q):
    S.append(input())
stack = []
for i in range(Q):
    if S[i] != "READ":
        stack.append(S[i])
    else:
        print(stack[-1])
        del stack[-1]

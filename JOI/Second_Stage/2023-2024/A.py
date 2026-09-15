N = int(input())
A = list(map(int, input().split()))
M = max(A)
kiroku = [False] * (M + 1)
flag = False
for a in A:
    kiroku[a] = True
for i in range(1, M - 5):
    if kiroku[i] and kiroku[i + 3] and kiroku[i + 6]:
        flag = True
if flag:
    print("Yes")
else:
    print("No")

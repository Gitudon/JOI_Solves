N, D = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
a_1 = []
a_2 = []
for i in range(2 * N):
    if i % 2 == 0:
        a_1.append(A[i])
    else:
        a_2.append(A[i])
flag = True
for i in range(N):
    if abs(a_1[i] - a_2[i]) > D:
        flag = False
if flag:
    print("Yes")
else:
    print("No")

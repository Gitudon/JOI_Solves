N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = []
while A != [] or B != []:
    if A == []:
        C.append(B[0])
        del B[0]
    elif B == []:
        C.append(A[0])
        del A[0]
    else:
        if A[0] > B[0]:
            C.append(B[0])
            del B[0]
        else:
            C.append(A[0])
            del A[0]
for i in range(len(C)):
    print(C[i])

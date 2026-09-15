N = int(input())
A = list(map(int, input().split()))
B = sorted(A)
for i in range(N):
    j = 0
    while A[i] > B[j]:
        j += 1
    print(j + 1)

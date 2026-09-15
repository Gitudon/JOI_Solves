N = int(input())
A, B = map(int, input().split())
C = int(input())
D = [0] * N
for i in range(N):
    D[i] = int(input())
D = sorted(D, reverse=True)
cal = C
val = A
ans = []
ans.append(C // A)
for i in range(N):
    cal += D[i]
    val += B
    ans.append(cal // val)
print(max(ans))

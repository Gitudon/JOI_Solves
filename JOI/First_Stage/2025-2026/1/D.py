N = int(input())
C = [0] * N
for i in range(N):
    C[i] = input().split()

ans = "No"
for i in range(N):
    flag = True
    for j in range(N - 1):
        if C[i][j] != C[i][j + 1]:
            flag = False
    if flag:
        ans = "Yes"

for j in range(N):
    flag = True
    for i in range(N - 1):
        if C[i][j] != C[i + 1][j]:
            flag = False
    if flag:
        ans = "Yes"

print(ans)

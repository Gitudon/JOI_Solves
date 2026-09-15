N, M = map(int, input().split())
flag = [0] * N
for i in range(N):
    flag[i] = input()
answer = 1000000000
for i in range(1, N):
    for j in range(i + 1, N):
        tmp = 0
        for k in range(0, i):
            for l in range(M):
                if flag[k][l] != "W":
                    tmp += 1
        for k in range(i, j):
            for l in range(M):
                if flag[k][l] != "B":
                    tmp += 1
        for k in range(j, N):
            for l in range(M):
                if flag[k][l] != "R":
                    tmp += 1
        if answer > tmp:
            answer = tmp
print(answer)

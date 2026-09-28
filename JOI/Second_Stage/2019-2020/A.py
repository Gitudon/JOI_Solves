N = int(input())
S = [0] * N
T = [0] * N
for i in range(N):
    S[i] = input()
for i in range(N):
    T[i] = input()


def kaiten(S, N):
    R = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            R[j][-(N - i)] = S[i][-(j + 1)]
    return R


def check(R, T, N):
    kaisu = 0
    for i in range(N):
        for j in range(N):
            if R[i][j] != T[i][j]:
                kaisu += 1
    return kaisu


ans = []
R1 = kaiten(S, N)
R2 = kaiten(R1, N)
R3 = kaiten(R2, N)
ans.append(check(S, T, N))
ans.append(1 + check(R1, T, N))
ans.append(2 + check(R2, T, N))
ans.append(1 + check(R3, T, N))
print(min(ans))

N = int(input())
K = N * (N - 1) // 2
A = [0] * K
for i in range(K):
    A[i] = list(map(int, input().split()))
team = [0] * N
for i in range(K):
    if A[i][2] > A[i][3]:
        team[A[i][0] - 1] += 3
        team[A[i][1] - 1] += 0
    elif A[i][2] < A[i][3]:
        team[A[i][0] - 1] += 0
        team[A[i][1] - 1] += 3
    else:
        team[A[i][0] - 1] += 1
        team[A[i][1] - 1] += 1
point = sorted(team, reverse=True)
for t in team:
    i = 0
    while point[i] != t:
        i += 1
    print(i + 1)

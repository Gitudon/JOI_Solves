A = list(map(int, input().split()))

team = [i for i in range(32)]

for i in range(4):
    next = []
    for i in range(len(team) // 2):
        if A[team[2 * i]] > A[team[2 * i + 1]]:
            next.append(team[2 * i])
        else:
            next.append(team[2 * i + 1])
    team = next

if A[team[0]] > A[team[1]]:
    print(team[1] + 1)
else:
    print(team[0] + 1)

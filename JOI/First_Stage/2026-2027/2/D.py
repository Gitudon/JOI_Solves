R, C = map(int, input().split())
S = [0] * R
for i in range(R):
    S[i] = input()

kiroku = set()
for i in range(R):
    for j in range(C):
        if S[i][j] == "U":
            if i != 0:
                if S[i - 1][j] == "D":
                    kiroku.add(f"(({i - 1}, {j}), ({i}, {j}))")
        elif S[i][j] == "D":
            if i != R - 1:
                if S[i + 1][j] == "U":
                    kiroku.add(f"(({i}, {j}), ({i + 1}, {j}))")
        elif S[i][j] == "L":
            if j != 0:
                if S[i][j - 1] == "R":
                    kiroku.add(f"(({i}, {j - 1}), ({i}, {j}))")
        elif S[i][j] == "R":
            if j != C - 1:
                if S[i][j + 1] == "L":
                    kiroku.add(f"(({i}, {j}), ({i}, {j + 1}))")

print(len(kiroku))

H, W = map(int, input().split())
kumo = [0] * H
for i in range(H):
    kumo[i] = input()
matrix = [[-1] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if kumo[i][j] == "c":
            matrix[i][j] = 0
        else:
            l = j
            while kumo[i][l] != "c" and l != -1:
                l -= 1
            if l != -1:
                matrix[i][j] = j - l
for i in range(H):
    print(*matrix[i])

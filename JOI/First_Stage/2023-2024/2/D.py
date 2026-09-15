X = int(input())
N = int(input())
i = 0
while X < N:
    r = X % 3
    if r == 0:
        X += 1
    elif r == 1:
        X *= 2
    else:
        X *= 3
    i += 1
print(i)

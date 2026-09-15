N = int(input())
K = int(input())
for i in range(K):
    a, b = map(int, input().split())
    if a <= b and (a + b) <= (N + 1):
        print((a - 1) % 3 + 1)
    elif a <= b and (a + b) > (N + 1):
        print((N - b) % 3 + 1)
    elif a > b and (a + b) < (N + 1):
        print((b - 1) % 3 + 1)
    else:
        print((N - a) % 3 + 1)

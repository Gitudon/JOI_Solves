X, Y, N = map(int, input().split())
print(X * (N % 2) + 2 * Y * (N // 2))

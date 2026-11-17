N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

dp = [0] * (N + 1)
for i in range(N):
    # 人iがペアを組まないとき
    dp[i + 1] = max(dp[i + 1], dp[i] + B[i])
    # 人iがペアを組むとき
    if i != 0:
        dp[i + 1] = max(dp[i + 1], dp[i - 1] + A[i - 1] + A[i])
print(dp[N])

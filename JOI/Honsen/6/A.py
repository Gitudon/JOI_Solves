n, k = map(int, input().split())
a = [0] * n
for i in range(n):
    a[i] = int(input())
current_sum = sum(a[:k])
max_sum = current_sum
for i in range(1, n - k + 1):
    current_sum = current_sum - a[i - 1] + a[i + k - 1]
    max_sum = max(max_sum, current_sum)
print(max_sum)

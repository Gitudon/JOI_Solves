N = int(input())
A = list(map(int, input().split()))
a = max(A)
mae = 0
i = 0
while A[i] != a:
    mae += A[i]
    i += 1
print(mae)
print(sum(A) - a - mae)

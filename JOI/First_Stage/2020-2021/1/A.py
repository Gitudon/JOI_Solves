A, B, C = map(int, input().split())

a = min(A, B, C)
b = max(A, B, C)

print(A + B + C - a - b)

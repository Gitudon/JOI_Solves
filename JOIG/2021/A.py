A, B, C = map(int, input().split())

a = max(A, B, C)
print((a - A) + (a - B) + (a - C))

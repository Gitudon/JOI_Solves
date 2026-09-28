N, A, B, C, D = map(int, input().split())

a = (N // A + 1) * B
if N % A == 0:
    a -= B
b = (N // C + 1) * D
if N % C == 0:
    b -= D

print(min(a, b))

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())

a = min(A, B, C, D)
b = A + B + C + D - a
c = max(E, F)

print(b + c)

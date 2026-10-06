A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

x = A * P
if P > C:
    y = B + (P - C) * D
else:
    y = B

print(min(x, y))

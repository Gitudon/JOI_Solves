a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())
m, n, o, p, q, r = map(int, input().split())

A = (d * 3600 + e * 60 + f) - (a * 3600 + b * 60 + c)
B = (j * 3600 + k * 60 + l) - (g * 3600 + h * 60 + i)
C = (p * 3600 + q * 60 + r) - (m * 3600 + n * 60 + o)

h1 = A // 3600
A -= 3600 * h1
m1 = A // 60
A -= 60 * m1
print(h1, m1, A)

h2 = B // 3600
B -= 3600 * h2
m2 = B // 60
B -= 60 * m2
print(h2, m2, B)

h3 = C // 3600
C -= 3600 * h3
m3 = C // 60
C -= 60 * m3
print(h3, m3, C)

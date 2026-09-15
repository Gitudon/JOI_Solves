N, A, B = map(int, input().split())
S = input()

a = S[: A - 1]
b = S[A - 1 : B]
c = S[B:]
d = len(b)
e = ""
for i in range(1, d + 1):
    e += b[-i]
print(a + e + c)

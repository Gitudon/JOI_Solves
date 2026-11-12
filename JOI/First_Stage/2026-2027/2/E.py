import math

N = int(input())
S = input()
M = int(input())
T = input()
K = int(input())

k = min(math.ceil(M / N) * 2, K)
X = S * k
if T in X:
    print("Yes")
else:
    print("No")

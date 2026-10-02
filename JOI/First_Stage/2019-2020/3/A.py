X, L, R = map(int, input().split())

if X < L:
    print(L)
elif L <= X <= R:
    print(X)
else:
    print(R)

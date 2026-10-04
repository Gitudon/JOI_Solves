ai, am, ac, ae = map(int, input().split())
bi, bm, bc, be = map(int, input().split())

S = ai + am + ac + ae
T = bi + bm + bc + be

if S >= T:
    print(S)
else:
    print(T)

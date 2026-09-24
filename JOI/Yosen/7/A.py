N = int(input())
O = 1000 - N
P = str(O)

if O >= 100:
    a = int(P[-3])
    b = int(P[-2])
    c = int(P[-1])
    if a >= 5:
        a -= 4
    if b >= 5:
        b -= 4
    if c >= 5:
        c -= 4
    ans = a + b + c
    print(ans)

elif 10 <= O < 100:
    b = int(P[-2])
    c = int(P[-1])
    if b >= 5:
        b -= 4
    if c >= 5:
        c -= 4
    ans = b + c
    print(ans)

elif O < 10:
    c = int(P[-1])
    if c >= 5:
        c -= 4
    ans = c
    print(ans)

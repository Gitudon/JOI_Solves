S = int(input())
A = int(input())
B = int(input())

if A >= S:
    print(250)
else:
    if (S - A) % B == 0:
        a = (S - A) // B
    else:
        a = ((S - A) // B) + 1
    print(250 + 100 * a)

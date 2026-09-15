n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
a = sorted(a)
b = []
for i in range(2 * n):
    if i + 1 not in a:
        b.append(i + 1)
b = sorted(b)
c = 0
while True:
    if b == [] or a == []:
        break
    for i in range(len(a) + 1):
        if i == len(a):
            c = 0
            break
        elif a[i] > c:
            c = a[i]
            a.remove(c)
            break
    if b == [] or a == []:
        break
    for i in range(len(b) + 1):
        if i == len(b):
            c = 0
            break
        elif b[i] > c:
            c = b[i]
            b.remove(c)
            break
if a == []:
    print(len(b))
    print(0)
else:
    print(0)
    print(len(a))

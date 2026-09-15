a = [0] * 28
for i in range(28):
    a[i] = int(input())
for i in range(30):
    if i + 1 not in a:
        print(i + 1)

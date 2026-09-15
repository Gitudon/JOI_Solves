N = int(input())
S = input()
a = [0, 0, 0, 0, 0]
b = ["A", "B", "C", "D", "E"]
for i in range(N):
    for j in range(5):
        if b[j] == S[i]:
            a[j] += 1
c = 0
for i in range(5):
    if a[i] != 0:
        c += 1
if c >= 3:
    print("Yes")
else:
    print("No")

a = input()
b = []
for i in range(len(a)):
    b.append(a[i])
for i in range(len(a)):
    if b[i] == "A":
        b[i] = "X"
    elif b[i] == "B":
        b[i] = "Y"
    elif b[i] == "C":
        b[i] = "Z"
    else:
        b[i] = chr(ord(b[i]) - 3)
c = ""
for i in range(len(a)):
    c += b[i]
print(c)

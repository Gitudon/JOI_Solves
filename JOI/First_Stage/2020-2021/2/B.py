N = int(input())
S = input()
I = False
O = False
I2 = False
for i in range(N):
    if S[i] == "I" and not I:
        I = True
    if I and not O and S[i] == "O":
        O = True
    if I and O and not I2 and S[i] == "I":
        I2 = True
if I and O and I2:
    print("Yes")
else:
    print("No")

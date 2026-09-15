N = int(input())
S = input()
T = input()

aoi = 0
bitaro = 0
for i in range(N):
    if S[i] == "R" and T[i] == "P":
        bitaro += 1
    elif S[i] == "S" and T[i] == "R":
        bitaro += 1
    elif S[i] == "S" and T[i] == "P":
        aoi += 1
print(aoi, bitaro)

N, K = map(int, input().split())
T = input()

a = T[: K - 1]
b = ""
for i in range(K, N + 1):
    if ord(T[i - 1]) == 106:
        b += "J"
    elif ord(T[i - 1]) == 111:
        b += "O"
    elif ord(T[i - 1]) == 105:
        b += "I"
    elif ord(T[i - 1]) == 74:
        b += "j"
    elif ord(T[i - 1]) == 79:
        b += "o"
    elif ord(T[i - 1]) == 73:
        b += "i"
print(a + b)

A = int(input())
B = int(input())

sum = A + B
ans = sum % 12
if ans == 0:
    ans = 12
print(ans)

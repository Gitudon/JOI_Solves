A, B, C = map(int, input().split())
i = 0
get = 0
while get < C:
    i += 1
    get += A
    if i % 7 == 0:
        get += B
print(i)

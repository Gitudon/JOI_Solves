n = int(input())

factors = {}
i = 2
temp = n
while i * i <= temp:
    count = 0
    while temp % i == 0:
        temp //= i
        count += 1
    if count > 0:
        factors[i] = count
    i += 1
if temp > 1:
    factors[temp] = 1

result = 0
for p in factors:
    e = factors[p]
    low = 1
    high = n
    while low < high:
        mid = (low + high) // 2
        count = 0
        power = p
        while power <= mid:
            count += mid // power
            power *= p

        if count >= e:
            high = mid
        else:
            low = mid + 1

    if low > result:
        result = low

print(result)

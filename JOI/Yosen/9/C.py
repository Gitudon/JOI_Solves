n = int(input())
m = int(input())
myfriends = []
others1 = []
others2 = []
for i in range(m):
    a, b = map(int, input().split())
    if a == 1:
        myfriends.append(b)
    elif b == 1:
        myfriends.append(a)
    else:
        others1.append(a)
        others2.append(b)
theirfriends = []
for i in range(len(others1)):
    if (
        others1[i] in myfriends
        and others2[i] not in theirfriends
        and others2[i] not in myfriends
    ):
        theirfriends.append(others2[i])
    elif (
        others2[i] in myfriends
        and others1[i] not in theirfriends
        and others1[i] not in myfriends
    ):
        theirfriends.append(others1[i])
print(len(myfriends) + len(theirfriends))

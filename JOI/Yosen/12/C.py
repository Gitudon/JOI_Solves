N = int(input())
name = input()
ans = 0
for i in range(N):
    tf = False
    kanban = input()
    for j in range(len(kanban)):
        for k in range(1, len(kanban) - j):
            kiritori = ""
            ichi = j
            while ichi < len(kanban):
                kiritori += kanban[ichi]
                ichi += k
                if kiritori == name:
                    tf = True
    if tf:
        ans += 1
print(ans)

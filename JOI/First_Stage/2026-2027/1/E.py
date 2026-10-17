S = input()
ans = "Yes"
i = 0
N = len(S)

while True:
    # 最後の文字まで行った
    if i == N:
        break
    # 次追加する文字が3文字未満
    elif N - i < 3:
        ans = "No"
        break
    # 次の3文字がJOI
    if S[i : i + 3] == "JOI":
        # 次の4文字がJOIG
        if i <= N - 4:
            if S[i + 3] == "G":
                i += 4
            else:
                i += 3
        else:
            i += 3
    # 次の3文字がIOI
    elif S[i : i + 3] == "IOI":
        i += 3
    else:
        ans = "No"
        break
print(ans)

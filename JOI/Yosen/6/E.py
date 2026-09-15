a, b, c = map(int, input().split())
N = int(input())

# 2...グレー
# 1...確実に正常
# 0...確実に故障
kosyo = [2] * (a + b + c + 1)

i_list = [0] * N
j_list = [0] * N
k_list = [0] * N
r_list = [0] * N

for i in range(N):
    i_list[i], j_list[i], k_list[i], r_list[i] = map(int, input().split())

# 全部正常
for i in range(N):
    if r_list[i] == 1:
        kosyo[i_list[i]] = 1
        kosyo[j_list[i]] = 1
        kosyo[k_list[i]] = 1

while True:
    buf = kosyo.copy()
    for i in range(N):
        if r_list[i] == 0:
            # 2つ1, 1つ2なら故障品がわかる
            if [kosyo[i_list[i]], kosyo[j_list[i]], kosyo[k_list[i]]].count(1) == 2:
                if kosyo[i_list[i]] != 1:
                    kosyo[i_list[i]] = 0
                elif kosyo[j_list[i]] != 1:
                    kosyo[j_list[i]] = 0
                elif kosyo[k_list[i]] != 1:
                    kosyo[k_list[i]] = 0
    if kosyo == buf:
        break

for i in range(1, a + b + c + 1):
    print(kosyo[i])

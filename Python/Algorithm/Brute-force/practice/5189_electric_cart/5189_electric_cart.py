# import sys
# sys.stdin = open("input.txt", "r")

def f(i, N, s):
    global min_num
    if i == N:
        temp = s + e[p[N-1]][0]
        if min_num > temp:
            min_num = temp

    elif min_num <= s:  # 가지치기
        return

    else:
        for j in range(N):
            if used[j] == 0:
                used[j] = 1
                p[i] = j
                f(i+1, N, s + e[p[i-1]][j])
                used[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]

    p = [0] * N
    used = [0] * N
    p[0] = 0
    used[0] = 1
    min_num = 1000

    f(1, N, 0)
    print(f'#{tc} {min_num}')




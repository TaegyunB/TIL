def is_babygin():
    tri = ru = 0
    if p[0] == p[1] == p[2]:
        tri += 1

    if p[3] == p[4] == p[5]:
        tri += 1

    if p[0] + 2 == p[1] + 1 == p[2]:
        ru += 1

    if p[3] + 2 == p[4] + 1 == p[5]:
        ru += 1

    if tri+ru == 2:
        return True
    else:
        return False

def f(i, N):
    global ans
    if i == N:
        if is_babygin():
            ans = "Baby Gin"

    else:
        for j in range(N):
            if used[j] == 0:
                used[j] = 1
                p[i] = a[j]
                f(i+1, N)
                # 돌아오면서 해야 할 로직
                used[j] = 0


T = int(input())

for tc in range(1, T+1):
    a = list(map(int, input()))
    used = [0] * 6  # visited랑 비슷한 방식
    p = [0] * 6
    ans = "Lose"

    f(0, 6)

    print(f'#{tc} {ans}')


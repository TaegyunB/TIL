# import sys
# sys.stdin = open("input1.txt", "r")

def min_sum(i, j, s):
    global min_v
    # 마지막에 도달했을 때
    if i == N-1 and j == N-1:
        if min_v > s + arr[i][j]:
            min_v = s + arr[i][j]
            return  # 재귀를 실행하면서 이제 앞으로 갈 수 없으면 실행했던 전 함수로 이동
    else:
        if i+1 < N:  # 아래
            min_sum(i+1, j, s+arr[i][j])

        if j+1 < N:  # 오른쪽
            min_sum(i, j+1, s+arr[i][j])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 1000

    min_sum(0, 0, 0)

    print(f'#{tc} {min_v}')



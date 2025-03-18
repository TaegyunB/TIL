# import sys
# sys.stdin = open("input.txt", "r")

def f(row, percent):
    global max_percent

    if row == N:
        percent = percent * 100
        if percent > max_percent:
            max_percent = percent
        return

    for i in range(N):
        if not visited[i]:
            f(row, percent * (work_success_rate[row][i] * 0.01))


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    work_success_rate = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N

    max_percent = 0
    f(0, 0)


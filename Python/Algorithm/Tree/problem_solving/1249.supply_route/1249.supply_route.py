# import sys
# sys.stdin = open("input.txt", "r")

import heapq

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dijkstra():
    pq = [(0, 0, 0)]  # 우선순위 큐 초기화: (비용, x좌표, y좌표)
    dists = [[float('inf')] * N for _ in range(N)]  # 각 칸까지의 최소 비용을 저장할 2차원 배열
    dists[0][0] = 0  # 시작점의 비용은 0

    while pq:
        cost, x, y = heapq.heappop(pq)  # 현재 가장 비용이 적은 위치 선택

        for i in range(4):  # 4방향으로 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            # 격자 범위를 벗어나면 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            # 새로운 비용 계산
            new_cost = arr[nx][ny] + dists[x][y]

            # 도착점에 도달했다면 비용 반환
            if nx == N-1 and ny == N-1:
                return new_cost

            # 이미 더 적은 비용으로 방문한 적 있다면 패스
            if dists[nx][ny] <= new_cost:
                continue

            # 최소 비용 개신 및 우선순위 큐에 추가
            dists[nx][ny] = new_cost
            heapq.heappush(pq, (new_cost, nx, ny))

    # 모든 탐색 후 도착점까지의 최소 비용 반환
    return dists[N-1][N-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    answer = dijkstra()

    print(f'#{tc} {answer}')
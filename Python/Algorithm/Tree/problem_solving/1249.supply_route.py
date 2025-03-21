import heapq

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dijkstra():
    dists = [[int(21e8)] * N for _ in range(N)]
    dists[0][0] = 0  # 시작점 초기화

    pq = [(0, 0, 0)]  # (dist - 누적거리, y, x) 형태

    while pq:
        dist, y, x = heapq.heappop(pq)

        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]

            # 범위 밖이면 continue
            if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N:
                continue

            # 누적 거리 계산
            new_dist = dists[y][x] + graph[new_y][new_x]
            # 이미 더 작거나 같은 시간으로 온 적이 있으면 continue
            if dists[new_y][new_x] <= new_dist:
                continue

            if new_y == N - 1 and new_x == N - 1:
                return new_dist

            dists[new_y][new_x] = new_dist
            heapq.heappush(pq, (new_dist, new_y, new_x))

    return dists[N - 1][N - 1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]

    result = dijkstra()
    print(f'#{tc} {result}')

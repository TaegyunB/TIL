# import sys
# sys.stdin = open("input.txt", "r")

import heapq

def dijkstra(N):

    # 4방향 이동
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    dists = [[INF] * N for _ in range(N)]  # 각 위치까지의 최소 비용 저장
    dists[0][0] = 0  # 시작점 비용은 0

    # 우선순위 큐: (비용, 행, 열)
    pq = [(0, 0, 0)]

    while pq:
        cost, r, c = heapq.heappop(pq)  # 현재 최소 비용 노드 꺼내기

        # 이미 처리된 지점이면 스킵 (더 적은 비용으로 이미 방문)
        if cost > dists[r][c]:
            continue

        # 도착지점에 도착했으면 종료
        if r == N-1 and c == N-1:
            return cost

        # 인접한 4방향 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 격자 범위 안에 있는지 확인
            if 0 <= nr < N and 0 <= nc < N:
                # 높이 차이 계산
                w = graph[nr][nc] - graph[r][c]

                # 높이가 같거나 낮으면 추가 비용 없음
                if w < 0:
                    w = 0

                # 총 비용 = 현재까지 비용 + 높이 차이 비용 + 기본 이동 비용(1)
                new_cost = cost + w + 1

                # 더 적은 비용으로 갈 수 있으면 업데이트
                if new_cost < dists[nr][nc]:
                    dists[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))  # heapq.heappush(리스트이름, 추가할 요소)

    return dists[N-1][N-1]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = []  # 각 위치의 높이 정보 저장
    INF = int(21e8)  # 무한대 값 설정

    # 격자의 높이 정보 입력받기
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    result = dijkstra(N)
    print(f'#{tc} {result}')



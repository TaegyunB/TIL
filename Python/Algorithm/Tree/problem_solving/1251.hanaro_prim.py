
import heapq

def prim(tax):
    pq = [(0, 0)]  # (비용, 노드) 형태로 저장
    visited = [0] * N  # 방문 여부 기록
    min_cost = 0  # 최소 비용

    dists = [float('inf')] * N  # 최소 비용 저장 리스트
    dists[0] = 0  # 시작점 비용은 0

    while pq:
        # cost 가 가장 저렴한 후보부터 나온다.
        cost, node = heapq.heappop(pq)

        if visited[node]:
            continue

        # node 로 가는 간선을 확정짓는 코드
        visited[node] = 1
        min_cost += cost

        for next_node in range(N):
            if visited[next_node]:
                continue

            # ((x좌표 차이 ** 2) + (y좌표 차이 ** 2)) * tax
            new_cost = ((x_list[next_node] - x_list[node]) ** 2 +
                        (y_list[next_node] - y_list[node]) ** 2) \
                       * tax

            # 우선순위큐에 삽입된 거리를 저장하면서 진행
            # - 더 작은 비용으로 갈 수 있을 때만 heapq 에 삽입
            if new_cost < dists[next_node]:
                dists[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

    return round(min_cost)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax = float(input())

    result = prim(tax)
    print(f'#{tc} {result}')

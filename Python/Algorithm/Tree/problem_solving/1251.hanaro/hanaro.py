# import sys
# sys.stdin = open("input.txt", "r")

import heapq

def prim(tax):
    pq = [(0, 0)]  # (비용, 노드)
    visited = [0] * N  # 방문 여부를 체크하는 배열
    min_cost = 0  # 최소 비용

    dist = [float('inf')] * N  # 각 노드까지의 최소 비용을 저장하는 배열
    dist[0] = 0  # 시작 노드의 비용은 0

    while pq:
        cost, node = heapq.heappop(pq)  # 가장 비용이 작은 간선 정보를 가져옴

        if visited[node]:  # 이미 방문한 노드라면 스킵
            continue

        visited[node] = 1  # 노드를 방문 처리
        min_cost += cost  # 최소 비용에 현재 간선의 비용을 더함

        for next_node in range(N):  # 모든 다른 노드에 대해
            if visited[next_node]:  # 이미 방문한 노드라면 스킵
                continue

            # 환경 부담금 정책
            new_cost = ((x_list[next_node] - x_list[node]) ** 2 +
                        (y_list[next_node] - y_list[node]) ** 2) * tax

            if new_cost < dist[next_node]:  # 더 적은 비용으로 갈 수 있다면
                dist[next_node] = new_cost  # 최소 비용 갱신
                heapq.heappush(pq, (new_cost, next_node))  # 우선순위 큐에 추가

    return round(min_cost)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax = float(input())

    answer = prim(tax)

    print(f'#{tc} {answer}')

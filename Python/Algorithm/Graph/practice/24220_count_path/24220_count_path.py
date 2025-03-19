# import sys
# sys.stdin = open("input.txt", "r")

def dfs(S):
    global cnt

    if S == end_node:  # 현재 노드가 도착 노드인 경우
        cnt += 1  # 경로 카운트 증가
        return

    for next_node in adj_list[S]:  # 현재 노드에서 이동 가능한 모든 다음 노드에 대해
        if visited[next_node] == 0:  # 다음 노드를 아직 방문하지 않았다면
            visited[next_node] = 1  # 다음 노드를 방문 표시
            dfs(next_node)  # 다음 노드로 재귀적으로 탐색 계속
            visited[next_node] = 0  # 백트래킹: 방문 표시 제거


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())  # N: 노드 수, E: 간선 수
    adj_node = list(map(int, input().split()))  # 간선 정보를 담은 배열
    start_node, end_node = map(int, input().split())

    # 연결 리스트 생성: 각 노드에서 이동 가능한 다음 노드들의 리스트
    adj_list = [[] for _ in range(N+1)]
    for i in range(E):
        adj_list[adj_node[2*i]].append(adj_node[2*i+1])  # 방향 그래프 생성: 2i는 출발 노드, 2i+1은 도착 노드

    visited = [0] * (N+1)
    cnt = 0
    dfs(start_node)
    print(f'#{tc} {cnt}')
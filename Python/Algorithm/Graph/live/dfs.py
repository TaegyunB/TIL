import sys
sys.stdin = open("graph.txt", "r")


def dfs(node):
    # 보통 그래프 문제들에서
    # ex) K개의 노드 방문했다면 종료
    # ex) N개를 모두 방문했다면 경로 출력
    # if 종료 시 해야할 것들 or 가지치기:
    #   return

    print(node, end=" ")

    # 현재 노드에서 인접한 노드들을 모두 확인하면서, 한 군데로 진행
    for next_node in graph[node]:
        # 이미 방문했다면 가지마라
        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node)


N, M = map(int, input().split())
# 1. 그래프를 저장하기
# - 비어있는 그래프를 생성함
# - 그래프 정보를 입력받아 넣음

# graph = [[0] * (N + 1) for _ in range(N)]  # 인접 행렬 (N * N의 0배열)
graph = [[] for _ in range(N+1)]  # 인접 리스트 (N * N ([]))

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)  # 양뱡향이라면, 뒤집에서 저장도 해주어야 함

visited = [0] * (N+1)  # 방문 여부 기록
visited[1] = 1  # 출발점 초기화
dfs(1)




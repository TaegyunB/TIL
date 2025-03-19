# import sys
# sys.stdin = open("input.txt", "r")


def dfs(n):
    for next_node in adj_list[n]:  # 현재 노드와 연결된 모든 인접 노드를 순회
        if visited[next_node] == 0:  # 아직 방문하지 않은 인접 노드라면
            visited[next_node] = 1  # 해당 노드를 방문했다고 표시
            dfs(next_node)  # 해당 노드에서 다시 DFS 탐색을 계속함


T = int(input())
for tc in range(1, T+1):
    std_num, pair = map(int, input().split())
    pair_list = list(map(int, input().split()))

    adj_list = [[] for _ in range(std_num + 1)]
    visited = [0] * (std_num + 1)

    for i in range(len(pair_list)//2):
        # 양방향 간선 추가 (무방향 그래프)
        adj_list[pair_list[2*i]].append(pair_list[2*i+1])
        adj_list[pair_list[2*i+1]].append(pair_list[2*i])

    team_cnt = 0
    for i in range(1, std_num+1):
        if visited[i] == 0:  # 아직 방문하지 않은 학생이라면
            visited[i] = 1  # 방문 표시
            dfs(i)  # 해당 학생부터 DFS 시작
            team_cnt += 1  # 하나의 조 완성

    print(f'#{tc} {team_cnt}')


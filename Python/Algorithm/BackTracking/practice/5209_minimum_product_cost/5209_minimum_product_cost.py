import sys
sys.stdin = open("input1.txt", "r")

def dfs(row, cost):
    """
    깊이 우선 탐색(DFS)으로 최소 비용을 찾는 함수
    """

    global min_num  # 전역 변수로 선언된 최소 비용

    # 백트래킹: 현재 비용이 이미 찾은 최소 비용보다 크거나 같으면 더 이상 탐색하지 않음
    if cost >= min_num:
        return

    elif row == N:  # 모든 작업(N개)을 처리했을 때
        min_num = min(min_num, cost)  # 현재 비용과 기존 최소 비용 중 작은 값으로 갱신
        return

    else:
        for i in range(N):  # 각 열에 대해
            if not visited[i]:  #  visited[i] = True 아직 방문하지 않았다면
                # 방문 표시
                dfs(row + 1, cost + arr[row][i])  # 재귀호출
                visited[i] = False  # 백트래킹: 방문 해제


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    min_num = 99*15

    dfs(0, 0)
    print(f'#{tc} {min_num}')
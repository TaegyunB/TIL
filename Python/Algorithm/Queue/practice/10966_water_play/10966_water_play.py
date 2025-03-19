# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

def bfs():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque()  # BFS를 위한 큐 생성
    visited = [[-1] * M for _ in range(N)]  # 방문 배열 초기화, -1은 미방문을 의미

    # 모든 물(W) 위치를 찾아 큐에 추가하고 거리를 0으로 초기화
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                q.append((i, j))
                visited[i][j] = 0

    # BFS 탐색 시작
    while q:
        x, y = q.popleft()  # 큐에서 현재 위치 꺼내기

        # 4방향 탐색
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 범위 내에 있고 아직 방문하지 않은 칸이라면
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1  # 이동 거리 갱신 (현재 위치 거리 + 1)
                q.append((nx, ny))  # 다음 탐색을 위해 큐에 추가

    # 모든 땅(L)에 대한 최소 이동 거리 합 계산
    total = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'L':
                total += visited[i][j]  # 땅 위치에서의 최소 이동 거리를 더함

    return total


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    result = bfs()

    print(f'#{tc} {result}')



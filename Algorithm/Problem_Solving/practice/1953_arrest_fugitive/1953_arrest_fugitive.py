'''
맨홀 뚜껑으로부터 출발
    - 터널들을 이동
    => 이동할 수 있는 개수를 구하라
        - 이동 방향: 상하좌우
            -> 델타 배열이 생각난다
        - 이동 못하는 경우
            -> 현재 내 위치에서 뚫려있는 곳으로만 가능
            -> 다음 위치의 입구가 뚫려있는 곳으로만 가능

이차원 리스트 형태 + 미로 탐색 문제 유형
- 우리가 배운 알고리즘 종류 (DFS, BFS)
    - 일단 끝까지 가보자 (DFS)
        - 재귀호출이 최악의 경우 2500번 발생 가능
        - 파이썬의 재귀 호출 기본 제한은 1000번
    - 주변으로 퍼져나가면서 확인하자(BFS)
        - 이 문제는 BFS로 푸는 게 쉽겠구나

- BFS
    - Queue를 활용해서 먼저 방문한 노드부터 탐색을 시작
        - 먼저 방문한 노드에서 갈 수 있는 노드들을 후보군에 추가


- BFS의 시간복잡도
    - O(V+E)
        - V: 정점의 개수 / E: 간선의 개수
        - 정점의 개수 = 2500개
            - queue에 최대 2500개까지 들어갈 수 잇음
                -> 여유롭구나
        - 간선의 개수 = 2500 * 4 = 10000개
'''
import sys
sys.stdin = open("input.txt", "r")

# 1. BFS로 접근
# - 이동 방향: 상하좌우
# - 이동이 불가능한 케이스
#   - [델타 배열 기본] 범위 밖으로 나가면 못감
#   - [방문 기록 기본] 이미 방문한 곳은 안감
#   - [문제 조건]
#       - 현재 내 위치에서 뚫려있는 곳으로만 이동 가능
#       - 다음 가려는 곳의 터널이 뚫려있는 곳으로만 이동 가능
#       -> 이런 케이스는 델타 배열 순서와 동일하게, 이동 가능 여부를 기록해두면 좋음

# 2. 방문 기록을 해야함(visited)

def f(N, M, R, C, L):
    q = [(R, C)]
    v = [[0] * M for _ in range(N)]
    v[R][C] = 1  # 시간
    # pos = [0] *(L+1)  # 시간대별 가능 위치 수
    cnt = 0
    while q:
        i, j = q.pop(0)
        cnt += 1
        # pos[v[i][j]] += 1 # 시간대에 도착하는 칸 번호
        if v[i][j] < L:  # L초 미만에 도착한 칸이면
            for x in pipe[tunnel[i][j]]:  # 파이프 모양에 따라 새롭게 진입할 칸 확인
                ni = i + di[x]
                nj = j + dj[x]
                if 0 <= ni < N and 0 <= nj < M and tunnel[ni][nj] != 0 and v[ni][nj] == 0 and (x + 2) % 4 in pipe[
                    tunnel[ni][nj]]:
                    v[ni][nj] = v[i][j] + 1  # 이동할 수 있는 칸에 시간
                    q.append((ni, nj))
    # return sum(pos)
    return cnt


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
pipe = [[], [0, 1, 2, 3], [1, 3], [0, 2], [0, 3], [0, 1], [1, 2], [2, 3], ]

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    r = f(N, M, R, C, L)
    print('#{} {}'.format(tc, r))





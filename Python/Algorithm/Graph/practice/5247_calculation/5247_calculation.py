# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

def bfs(start, end):
    q = deque([start])  # 시작 숫자를 큐에 넣고 BFS 시작
    visited = [0] * 1000001  # 각 숫자에 도달하는데 필요한 연산 횟수를 저장할 배열

    while q:  # 큐가 빌 때까지 반복
        chk = q.popleft()  # 큐에서 현재 숫자를 꺼냄
        calculation = [chk+1, chk-1, chk*2, chk-10]  # 현재 숫자에 적용할 수 있는 4가지 연산

        for cal in calculation:  # 각 연산 결과에 대해
            if cal == end:  # 목표 숫자에 도달했다면
                return visited[chk] + 1  # 현재까지의 연산 횟수 + 1 반환
            elif 0 < cal < 1000001 and visited[cal] == 0:  # 유효한 범위 내이고 아직 방문하지 않았다면
                visited[cal] = visited[chk] + 1  # 현재까지의 연산 횟수 + 1을 저장
                q.append(cal)  # 다음 단계에서 탐색하기 위해 큐에 추가


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    answer = bfs(N, M)

    print(f'#{tc} {answer}')
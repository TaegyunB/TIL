# import sys
# sys.stdin = open("input.txt", "r")

def check(row, col):
    """
    현재 위치(row, col)에 퀸을 놓을 수 있는지 확인하는 함수
    퀸은 같은 열, 같은 대각선에 있는 다른 퀸을 공격할 수 있으므로
    해당 위치에 퀸을 놓을 수 있는지 검사
    """

    # 같은 열에 놓은 적이 있는지
    # 이미 같은 열에 퀸이 있으면 False 반환
    for i in range(row):
        if chess[i][col]:
            return False

    # 왼쪽 대각선(\) 방향으로 퀸이 있는지 확인
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if chess[i][j]:
            return False  # 대각선에 퀸이 있으면 False 반환

        i -= 1
        j -= 1

    # 오른쪽 대각선(/) 방향으로 퀸이 있는지 확인
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if chess[i][j]:
            return False  # 대각선에 퀸이 있으면 False 반환

        i -= 1
        j += 1

    return True  # 모든 검사를 통과하면 퀸을 놓을 수 있음


def dfs(row):
    """
    깊이 우선 탐색(DFS)을 사용하여 각 행에 퀸을 놓는 함수
    row: 현재 처리 중인 행
    """

    global answer

    # 모두 놓으면 성공
    if row == N:
        answer += 1  # 경우의 수 증가
        return

    # 현재 행의 각 열에 퀸을 놓아보기
    for col in range(N):
        if check(row, col) is False:
            continue  # 해당 위치에 퀸을 놓을 수 없으면 다음 열로

        # 퀸을 놓고
        chess[row][col] = 1
        # 다음 행으로 재귀 호출
        dfs(row + 1)
        # 백트래킹: 퀸을 제거하고 다른 위치 시도
        chess[row][col] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    chess = [[0] * N for _ in range(N)]
    answer = 0

    dfs(0)  # 0행부터 시작하여 DFS 실행
    print(f'#{tc} {answer}')
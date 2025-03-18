import sys
sys.stdin = open("input.txt", "r")

def f(row, percent):
    """
    현재 직원(row)에게 작업으 할당하는 백트래킹 함수
    """
    global max_percent

    # 가지치기(백트래킹)
    if percent <= max_percent:
        return

    # 모든 직원에게 일이 할당된 경우
    if row == N:
        # 최대 성공 확률 업데이트
        max_percent = max(max_percent, percent)
        return

    # 각 일을 순회하면서 해당 직원이 담당할 경우를 고려
    for i in range(N):
        if not visited[i]:  # 아직 할당되지 않은 일이면 선택
            visited[i] = True  # 선택한 일을 할당
            # 현재 확률에 해당 직원이 해당 일을 성공할 확률을 곱한 값을 전달하여 다음 단계 탐색
            f(row+1, percent * (work_success_rate[row][i] * 0.01))
            visited[i] = False  # 백트래킹: 원래 상태로 복구


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    work_success_rate = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N

    max_percent = 0
    f(0, 1)

    print(f'#{tc} {max_percent*100:.6f}')  # 확률을 퍼센트 단위로 변환하고 소수점 6자리까지 출력
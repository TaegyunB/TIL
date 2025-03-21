# import sys
# sys.stdin = open("input.txt", "r")

def cal_synergy(lst):
    """
    주어진 재료 리스트에 대한 시너지 총합을 계산하는 함수
    """
    total = 0
    # 음식이 3개 이상이면, 각각의 시너지들을 모두 더해주어야 함
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            # 두 재료 간의 양방향 시너지 값을 더함
            total += arr[lst[i]][lst[j]] + arr[lst[j]][lst[i]]

    return total


def get_synergy():
    """
    A와 B 두 그룹으로 나뉜 재료들의 시너지 값을 각각 계산하는 함수
    """

    A_list, B_list = [], []
    for i in range(N):
        if visited[i]:  # visited가 1이면 A팀 재료
            A_list.append(i)
        else:  # visited가 0이면 B팀 재료
            B_list.append(i)

    # 두 팀의 시너지 값을 계산하여 반환
    return cal_synergy(A_list), cal_synergy(B_list)


def dfs(cnt, a_cnt):
    """
    DFS를 이용하여 가능한 모든 재료 조합을 탐색하는 함수
    cnt: 현재까지 선택한 A팀 재료의 개수
    a_cnt: 다음에 선택할 수 있는 재료의 최소 인덱스
    """

    global answer

    # N/2개의 재료를 A팀에 배정했다면 시너지 차이 계산
    if cnt == N // 2:
        a_total, b_total = get_synergy()  # 각 팀의 시너지 총합 계산
        answer = min(answer, abs(a_total - b_total))  # 최소 차이 갱신
        return

    # 조합을 구하기 위한 재귀 호출(백트래킹)
    for food_num in range(a_cnt, N):
        if visited[food_num]:  # 이미 선택된 재료라면 스킵
            continue

        visited[food_num] = 1  # A팀에 재료 배정
        dfs(cnt + 1, food_num + 1)  # 다음 재료 선택
        visited[food_num] = 0  # 배정 취소(백트래킹)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N  # 특정 재료 사용 여부
    answer = 1e9
    dfs(0, 0)  # (초기 선택 개수, 시작 인덱스)
    print(f'#{tc} {answer}')
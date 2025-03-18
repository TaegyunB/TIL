arr = [i for i in range(1, 11)]
# visited = [] -> 이번 문제에서는 사용할 필요가 없음

# level: N개의 원소를 모두 고려하면
# branch: 집합에 해당 원소를 포함 시키는 경우 or 안 시키는 경우 두 가지
# 누적값
# - 부분집합의 총합
# - 부분집합에 포함된 원소들
def dfs(cnt, total, subset):
    # 1. total이 10이면 출력해라
    if total == 10:
        print(subset)
        return

    # 2. total이 10을 넘었으면 가지치기하자
    if total > 10:
        return

    if cnt == 10:
        return

    dfs(cnt + 1, total + arr[cnt], subset + [arr[cnt]])  # 포함 하는 경우
    dfs(cnt + 1, total, subset)#  집합에 포함 안하는 경우

dfs(0, 0, [])
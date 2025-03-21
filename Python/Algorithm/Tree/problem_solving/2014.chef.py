# 접근법
# 선택한 재료 A 음식에 넣고 선택 안 한 재료들은 B 음식에 넣자.
# -> 모든 재료를 골라보면서 A 에 넣고, 나머지를 B 로 넣자
# - visited 된 건 A에, visited 안된 건 B에 들어갔음
# -> 반만 고르면 끝임
def cal_synergy(lst):
    total = 0
    # 음식이 3개 이상이면, 각각의 시너지들을 모두 더해주어야 함
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            total += matrix[lst[i]][lst[j]] + matrix[lst[j]][lst[i]]
    return total


def get_synergy():
    A_list, B_list = [], []
    for i in range(N):
        if visited[i]:
            A_list.append(i)
        else:
            B_list.append(i)

    return cal_synergy(A_list), cal_synergy(B_list)


def dfs(cnt, a_cnt):
    global answer
    # 반에 해당하는 모든 조합을 A 에 넣어봄
    if cnt == N // 2:
        a_total, b_total = get_synergy()
        answer = min(answer, abs(a_total - b_total))
        return

    for food_num in range(a_cnt, N):
        if visited[food_num]:
            continue

        visited[food_num] = 1
        dfs(cnt + 1, food_num + 1)
        visited[food_num] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N  # 특정 재료 사용 여부
    answer = 1e9
    dfs(0, 0)
    print(f'#{tc} {answer}')

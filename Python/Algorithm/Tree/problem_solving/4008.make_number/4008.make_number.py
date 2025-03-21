import sys
sys.stdin = open("input.txt", "r")


def cal(num1, num2, oper_idx):
    if oper_idx == 0:
        return num1 + num2

    if oper_idx == 1:
        return num1 - num2

    if oper_idx == 2:
        return num1 * num2

    if oper_idx == 3:
        if num1 < 0:
            return -(abs(num1) // num2)
        return num1 // num2


def dfs(level, total):
    global max_num, min_num

    if level == N:
        min_num = min(min_num, total)
        max_num = max(max_num, total)
        return

    # 4개의 연산자를 확인
    for i in range(4):
        if operators[i] == 0:
            continue

        operators[i] -= 1
        dfs(level+1, cal(total, arr[level], i))
        operators[i] += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    operators = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    max_num = -100000000
    min_num = 100000000

    dfs(1, arr[0])
    print(f'#{tc} {max_num - min_num}')

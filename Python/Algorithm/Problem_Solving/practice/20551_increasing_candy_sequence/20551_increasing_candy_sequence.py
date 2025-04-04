# import sys
# sys.stdin = open("input.txt", "r")


def calculate(A, B, C):
    cnt = 0

    if B < 2 or C < 3:  # 어떤 방식으로 먹더라도 사탕의 개수가 순증가 할 수 없으면
        return -1

    while C <= B:  # C가 B보다 커질 때 까지
        B -= 1
        cnt += 1

    while B <= A:  # B가 A보다 커질 때 까지
        A -= 1
        cnt += 1

    return cnt


T = int(input())

for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    print(f'#{tc} {calculate(A, B, C)}')

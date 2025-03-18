import sys
sys.stdin = open("input1.txt", "r")

# T = int(input())
#
# for tc in range(1, T+1):
#     N, *arr = map(int, input().split())
#
#     i = 1
#     cnt = 0
#     last = N-1
#     cur = arr[0]
#
#     while i < N-1:
#         if arr[0] > N-1:
#             break
#
#         if cur < N-1:
#             max_num = 0
#             for j in range(i, i+cur+1):
#                 if cur < arr[j]:
#                     max_num = arr[j]
#
#                 i = j
#                 cur = arr[i]
#             cnt += 1
#
#     print(f'#{tc} {cnt}')

def dfs(stop):
    global ans
    if stop + bus[stop] >= N - 1:  # 충전지 합이 N이 되면 종료
        return

    next_stop = 0
    max_i = 0
    for i in range(stop + 1, stop + bus[stop] + 1):
        if next_stop < i + bus[i]:
            next_stop = i + bus[i]
            max_i = i
    ans += 1
    dfs(max_i)


T = int(input())
for tc in range(1, T + 1):
    N, *bus = map(int, input().split())
    ans = 0
    dfs(0)
    print(f"#{tc} {ans}")
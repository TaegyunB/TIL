import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pos_list = []
    cnt = 0
    for _ in range(N):
        x, y = map(int, input().split())
        pos_list.append([x, y])

    for i in range(0, len(pos_list)):
        for j in range(i+1, len(pos_list)):
            if pos_list[i][0] < pos_list[j][0] and pos_list[i][1] > pos_list[j][1]:
                cnt += 1
            elif pos_list[i][0] > pos_list[j][0] and pos_list[i][1] < pos_list[j][1]:
                cnt += 1

    print(f'#{tc} {cnt}')

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    total_room = [0] * 401

    for j in range(N):

        start_room, end_room = map(int, input().split())

        if start_room > end_room:
            start_room, end_room = end_room, start_room

        if start_room % 2 == 0:
            start_room -= 1

        for i in range(start_room, end_room+1):
            total_room[i] += 1

        max_num = 0
        for i in range(len(total_room)):
            if total_room[i] > max_num:
                max_num = total_room[i]

    print(f'#{tc} {max_num}')
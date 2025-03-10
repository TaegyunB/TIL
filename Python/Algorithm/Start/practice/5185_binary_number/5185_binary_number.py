import sys
sys.stdin = open("input1.txt", "r")

def hexadecimal_to_binary(target):
    hex_digit = "0123456789ABCDEF"
    hex_number = ""

    rev_target = ""
    for i in range(len(target)-1, -1, -1):
        rev_target += target[i]

    for x in rev_target:
        for i in range(len(hex_digit)):
            if x == hex_digit[i]:
                cnt = 0
                while i > 0:
                    remain = i % 2
                    hex_number = str(remain) + hex_number
                    i //= 2
                    cnt += 1

                if cnt != 4:
                    turn = 4 - cnt
                    for j in range(turn):
                        hex_number = '0' + hex_number

                # if i == 1:
                #     hex_number = str(i) + hex_number

    return hex_number


T = int(input())

for tc in range(1, T+1):
    N, hexadecimal = input().split()
    print(f'#{tc} {hexadecimal_to_binary(hexadecimal)}')

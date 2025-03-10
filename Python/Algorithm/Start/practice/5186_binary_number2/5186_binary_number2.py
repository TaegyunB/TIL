# import sys
# sys.stdin = open("input1.txt", "r")

def decimal_to_binary(target):
    result = ""

    for i in range(1, 14):
        if target == 0:
            return result
        elif target - (2 ** (-i)) >= 0:
            result += '1'
            target = target - (2 ** (-i))
        else:
            result += '0'

    if len(result) >= 13:
        return 'overflow'


T = int(input())

for tc in range(1, T+1):
    N = float(input())

    print(f'#{tc} {decimal_to_binary(N)}')

import sys
sys.stdin = open("input.txt", "r")

# 2진수로 변환
def to_binary(hex):
    hexadecimal = '0123456789ABCDEFG'
    binary = ""
    rev_hex = ""

    for i in range(len(hex)-1, -1, -1):
        rev_hex += hex[i]

    for x in rev_hex:
        for i in range(len(hexadecimal)):
            if x == hexadecimal[i]:
                cnt = 0
                while i > 0:
                    binary = str(i % 2) + binary
                    i //= 2
                    cnt += 1

                while cnt != 4:
                    binary = '0' + binary
                    cnt += 1

    return binary


def to_decimal(bin):
    result = ""

    for i in range(0, len(bin), 7):
        dec = ""
        if len(bin) - i < 7:
            break

        for j in range(i, i+7):
            dec += bin[j]

        rev_dec = reversed(dec)
        decimal_number = 0
        pow = 0  # 지수

        for digit in rev_dec:
            if digit == "1":
                decimal_number += 2 ** pow
            pow += 1

        result += str(decimal_number) + " "

    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    hex = input()

    print(f'#{tc}', end=" ")
    print(to_decimal(to_binary(hex)))





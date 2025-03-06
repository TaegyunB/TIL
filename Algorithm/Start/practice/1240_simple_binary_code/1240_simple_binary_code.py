import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] + list(input()) + [0] for _ in range(N)]

    secret_code = {0:"0001101", 1:"0011001", 2:"0010011", 3:"0111101", 4:"0100011", 5:"0110001", 6:"0101111", 7:"0111011", 8:"0110111", 9:"0001011"}

    secret_list = []

    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if arr[i][j] == "1":
                j -= 55

                for k in range(j, j+56, 7):
                    part_code = ""
                    for l in range(k, k+7):
                        part_code += str(arr[i][l])

                    for key, value in secret_code.items():
                        if part_code == value:
                            secret_list.append(key)  # 딕셔너리 키 값 추가
                            break
            if secret_list:
                break

        if secret_list:
            break

    sum_even = 0
    sum_odd = 0
    for i in range(len(secret_list)):
        if i % 2 == 0:
            sum_odd += secret_list[i]
        else:
            sum_even += secret_list[i]

    result = (sum_odd * 3) + sum_even

    answer = 0
    if result % 10 == 0:
        answer = sum_odd + sum_even

    print(f'#{tc} {answer}')

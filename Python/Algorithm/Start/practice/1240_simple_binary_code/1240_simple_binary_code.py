import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] + list(input()) + [0] for _ in range(N)]

    secret_code = {0:"0001101", 1:"0011001", 2:"0010011", 3:"0111101", 4:"0100011", 5:"0110001", 6:"0101111", 7:"0111011", 8:"0110111", 9:"0001011"}

    secret_list = []

    for i in range(N-1, -1, -1):  # 뒤에서 부터 탐색
        for j in range(M-1, -1, -1):
            if arr[i][j] == "1":  # 1을 찾으면 길이가 항상 총 54라고 했으니깐 지금 현재 칸 포함 j에 -55
                j -= 55  # 다시 앞에서 탐색하기 위함

                # 뺀 j값에서 시작
                for k in range(j, j+56, 7):
                    part_code = ""
                    for l in range(k, k+7):
                        part_code += str(arr[i][l])

                    for key, value in secret_code.items():
                        if part_code == value:
                            secret_list.append(key)  # 딕셔너리 키 값 추가
                            break

            # 한 줄만 계산하면 되니깐 secret_list에 값이 있으면 모든 for문에서 빠져나와야함
            if secret_list:
                break

        if secret_list:
            break

    sum_even = 0
    sum_odd = 0
    # 인덱스 0부터 시작했기 때문에 문제와 반대로 계산
    for i in range(len(secret_list)):
        if i % 2 == 0:  # 짝수일 때 문제에서 얘기한 홀수 값 더하기
            sum_odd += secret_list[i]
        else:  # 홀수일 때 문제에서 얘기한 짝수 값 더하기
            sum_even += secret_list[i]

    result = (sum_odd * 3) + sum_even

    answer = 0

    if result % 10 == 0:
        answer = sum_odd + sum_even

    print(f'#{tc} {answer}')

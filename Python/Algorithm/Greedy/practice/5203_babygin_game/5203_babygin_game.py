import sys
sys.stdin = open("input1.txt", "r")


# run 검사 - 연속된 3개 숫자
def check_run(arr):
    counts = [0] * 10

    for x in arr:
        counts[x] += 1

    cnt = 0
    for i in range(len(counts)):
        if counts[i] > 0:
            cnt += 1

            if cnt >= 3:
                return True
        else:
            cnt = 0

    return False

# triplet 검사 - 같은 숫자가 3개 이상
def check_triplet(arr):
    sorted_arr = sorted(arr)

    for i in range(len(sorted_arr) - 2):
        if sorted_arr[i] == sorted_arr[i+1] == sorted_arr[i+2]:
            return True

    return False

# babygin 검사
def is_babygin(arr):
    return check_run(arr) or check_triplet(arr)


T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    A = []
    B = []

    winner = 0
    for i in range(0, len(arr), 2):
        A.append(arr[i])

        if len(A) >= 3 and is_babygin(A):
            winner = 1
            break

        B.append(arr[i+1])

        if len(B) >= 3 and is_babygin(B):
            winner = 2
            break

    print(f'#{tc} {winner}')


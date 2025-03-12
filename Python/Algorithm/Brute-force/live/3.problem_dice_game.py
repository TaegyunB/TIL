# 주사위 3개를 던져 합이 10이하인 경우는 몇 개인가 ?
# 종료조건: 3번 던진다.
# 나올 수 있는 범위: 주사위는 1~6

path = []
result = 0


def recur(cnt, total):
    global result
    # 이미 10을 넘으면 더 이상 볼 필요가 없다.
    # 기저조건에서 경우의 수들을 많이 줄여주는 기법
    if total > 10:
        return

    if cnt == 3:
        # 합이 10 이하인건 몇 개인가 ?
        # sum: path 길이만큼 반복되기 때문에 비효율 (O(N))
        # if sum(path) <= 10:
        #     result += 1
        #     print(path)

        if total <= 10:
            result += 1
            print(path)
        return

    for num in range(1, 7):
        path.append(num)
        # 주사위 결과를 더해서 전달
        recur(cnt + 1, total + num)
        path.pop()


recur(0, 0)

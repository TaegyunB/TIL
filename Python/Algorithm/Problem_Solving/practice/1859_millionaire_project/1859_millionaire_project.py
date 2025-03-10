# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))

    # 뒤에서부터 접근하는 방식
    max_price = 0  # 현재까지의 최대 가격
    profit = 0  # 총 이익

    # 뒤에서부터 순회
    for i in range(N - 1, -1, -1):
        if price[i] > max_price:
            max_price = price[i]  # 최대 가격 갱신
        else:
            # 현재 가격이 최대 가격보다 낮으면, 최대값에서 현재 가격을 뺀 값을 이익에 추가
            profit += max_price - price[i]

    print(f'#{tc} {profit}')
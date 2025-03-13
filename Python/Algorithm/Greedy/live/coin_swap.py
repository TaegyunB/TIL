coin_list = [500, 100, 50, 10]  # 큰 동전부터 앞으로 작성함
target = 1730
cnt = 0

for coin in coin_list:
    possible_cnt = target // coin  # 현재 동전으로 가능한 최대 수
    cnt += target // coin  # 정답에 더해줌
    target -= coin * possible_cnt  # 금액을 빼 줌

print(cnt)
# [0, 1, 2] 3개의 카드가 존재
# 2개를 뽑을 예정

path = []       # 뽑은 카드들을 저장
# cnt = 재귀호출마다 누적되어서 전달되어야 하는 값
def recur(cnt):
    # 카드를 3개 뽑으면 종료
    if cnt == 3:
        # 종료 시에 해야할 로직들을 작성
        print(*path)
        return

    # 만약 카드가 1~6 까지 6개가 있다면 ?
    for num in range(1, 7):
        path.append(num)
        recur(cnt + 1)
        path.pop()

    # 카드 0~2
    # for num in range(3):
    #     path.append(num)
    #     recur(cnt + 1)
    #     path.pop()
    
    # # 1. 1개의 카드를 뽑는다
    # path.append(0)
    # # 2. 다음 재귀 호출 (뽑은 카드가 1개 추가되었다)
    # recur(cnt + 1)
    # path.pop()
    #
    # path.append(1)
    # recur(cnt + 1)
    # path.pop()
    #
    # path.append(2)
    # recur(cnt + 1)
    # path.pop()
    
    
# 제일 처음 호출할 때 시점이므로
# 초기값을 전달하면서 시작
recur(0)

path = []  # 뽑은 카드들을 저장
used = [False] * 7  # 1~6 숫자 사용 여부를 기록


# 조금 더 어려운 문제의 경우(숫자 범위가 매우 클 때)
# -> 위와 같은 리스트 방식은 메모리 초과 가능성이 존재
# -> dictionary(O(1)), set(O(1)) 이런 자료구조로 해결


def recur(cnt):
    # 카드를 2개 뽑으면 종료 -> 3개 뽑고 싶으면 cnt == 3으로 바꿔주면 됨
    if cnt == 3:
        # 종료 시에 해야할 로직들을 작성
        print(*path)
        return

    # 만약 카드가 1~6까지 6개가 있다면 ?
    for num in range(1, 7):
        # 이미 num을 뽑았다면 뽑지 마라
        # == num을 뽑지 않았을 때만 뽑아라.
        # if num in path:  # 이거의 단점: in은 O(N)번(전체검사를 하기 때문에 느림)-> 시간 초과 발생
        #     continue

        # 인덱스 검색 연산은 O(1)
        if used[num] is True:
            continue

        used[num] = True
        path.append(num)
        recur(cnt + 1)
        path.pop()
        used[num] = False

# 제일 처음 호출할 때 시점이므로
# 초기값을 전달하면서 시작
recur(0)

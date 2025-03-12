path = []       # 뽑은 카드들을 저장
used = [False] * 7  # 1~6 숫자 사용 여부를 기록
# 왜 7개죠 ? 숫자는 6개인데 ??
#  -> 그냥 0번 인덱스를 낭비하자! (편의를 위해)

# 조금 더 어려운 문제의 경우 (숫자 범위가 매우 크다)
# -> 위와 같은 리스트 방식은 메모리 초과 가능성이 존재
# -> dictionary(O(1)), set(O(1)) 이런 자료구조로 해결


def recur(cnt):
    # 카드를 3개 뽑으면 종료
    if cnt == 3:
        # 종료 시에 해야할 로직들을 작성
        print(*path)
        return

    # 만약 카드가 1~6 까지 6개가 있다면 ?
    for num in range(1, 7):
        # 이미 num 을 뽑았다면 뽑지 마라
        # == num 을 뽑지 않았을 때만 뽑아라.
        # in: path 를 전체검사하기 때문에 느리다!! O(N)
        # if num in path:
        #     continue

        # 인덱스 검색 연산은 O(1)
        if used[num] is True:
            continue

        used[num] = True
        path.append(num)
        recur(cnt + 1)
        path.pop()
        used[num] = False


recur(0)

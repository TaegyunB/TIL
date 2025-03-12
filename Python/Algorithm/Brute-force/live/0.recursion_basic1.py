def KFC(num):
    # 언제 재귀호출을 중지할까 ?
    # 재귀호출의 특징1. 항상 종료 조건과 함께 한다.
    if num == 3:
        return
    # 재귀 호출 전 들어가야 할 로직
    print(num, end=' ')
    KFC(num + 1)    # 다음 재귀 호출 (매개변수를 변경하면서 전달)
    # 돌아 오면서 해야 할 로직
    print(num, end=' ')

KFC(0)
print("끝")

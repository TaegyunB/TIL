def KFC(num):
    if num == 3:
        return
    
    # 4의 의미: 현재 시점에서 다음 케이스는 4개다.
    # (트리 그림에서 가지가 4개)
    for _ in range(4):
        print(num, end=' ')
        KFC(num + 1)
        print(num, end=' ')

KFC(0)
print("끝")

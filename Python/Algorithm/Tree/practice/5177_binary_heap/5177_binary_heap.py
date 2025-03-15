import sys
sys.stdin = open("input1.txt", "r")

# 원소를 힙에 삽입하는 함수
def enq(num):
    global last
    last += 1  # 마지막 노드 인덱스 증가

    tree[last] = num  # 새 노드를 마지막 위치에 추가
    c = last  # 현재 노드 위치
    q = c // 2  # 부모 노드 위치

    # 최소힙: 부모가 있고, 부모 값이 현재 값보다 크면 교환
    while q and tree[q] > tree[c]:
        tree[q], tree[c] = tree[c], tree[q]  # 부모와 자식 노드 교환
        c = q  # 현재 위치를 부모 위치로 이동
        q = c // 2  # 새로운 부모 위치 계산


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (N+1)

    last = 0
    for i in range(len(arr)):
        enq(arr[i])

    # 마지막 노드의 조상 노드 값들의 합 계산
    c = last // 2  # 마지막 노드의 부모 노드부터 시작
    ans = 0

    # 루트까지 올라가면서 모든 조상 노드 값 더하기
    while c > 0:
        ans += tree[c]  # 현재 노드 값 더하기
        c //= 2  # 부모 노드로 이동

    print(f'{tc} {ans}')
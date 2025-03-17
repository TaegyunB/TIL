import sys
sys.stdin = open("input.txt", "r")

def binary_search(left, right, target, dir):
    global cnt

    if left > right:  # 검색 범위가 없는 경우
        return  # 종료

    mid = (left + right) // 2  # 중간 지점 계산

    if A[mid] == target:  # 타겟을 찾은 경우
        cnt += 1  # 찾은 횟수 증가
        return  # 종료

    if target < A[mid]:  # 타겟이 중간값보다 작은 경우
        if dir == 'left':  # 이미 이전에 왼쪽으로 갔다면
            return  # 종료

        binary_search(left, mid-1, target, 'left')  # 왼쪽 부분에서 재귀적으로 검색

    elif target > A[mid]:  # 타겟이 중간값보다 큰 경우
        if dir == 'right':  # 이미 이전에 오른쪽으로 갔다면
            return  # 종료

        binary_search(mid+1, right, target, 'right')  # 오른쪽 부분에서 재귀적으로 검색


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()  # 이진 탐색은 항상 정렬되어 있는 상태여야 하기 때문에 A 배열 정렬

    cnt = 0

    for x in B:
        binary_search(0, N-1, x, "None")  # 초기 방향 없이 이진 탐색 수행

    print(f'#{tc} {cnt}')
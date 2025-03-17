# import sys
# sys.stdin = open("input.txt", "r")

def merge(left, right):
    global cnt
    result = [0] * (len(left) + len(right))  # 병합 결과를 저장할 배열 생성
    l = r = 0  # 왼쪽과 오른쪽 배열의 인덱스 초기화

    # 왼쪽 배열의 마지막 원소가 오른쪽 배열의 마지막 원소보다 큰 경우 카운트 증가
    if left[-1] > right[-1]:
        cnt += 1

    # 두 배열을 비교하여 작은 값부터 결과 배열에 저장
    while l < len(left) and r < len(right):

        if left[l] < right[r]:  # 왼쪽 배열의 원소가 더 작은 경우
            result[l+r] = left[l]  # 결과 배열에 왼쪽 배열의 원소 저장
            l += 1  # 왼쪽 배열 인덱스 증가

        else:  # 오른쪽 배열의 원소가 더 작거나 같은 경우
            result[l+r] = right[r]  # 결과 배열에 오른쪽 배열의 원소 저장
            r += 1  # 오른쪽 배열 인덱스 증가

    # 왼쪽 배열에 남은 원소가 있는 경우 결과 배열에 추가
    while l < len(left):
        result[l+r] = left[l]
        l += 1

    # 오른쪽 배열에 남은 우너소가 있는 경우 결과 배열에 추가
    while r < len(right):
        result[l+r] = right[r]
        r += 1

    return result


def merge_sort(li):
    if len(li) == 1: # 배열의 길이가 1인 경우 그대로 반환
        return li

    n = len(li)
    mid = n // 2
    left = li[:mid]  # 왼쪽 부분 배열
    right = li[mid:]  # 오른쪽 부분 배열

    # 재귀적으로 왼쪽과 오른쪽 부분 배열 정렬
    left_arr = merge_sort(left)
    right_arr = merge_sort(right)

    # 정렬된 왼쪽과 오른쪽 부분 배열을 병합
    merge_sort_result = merge(left_arr, right_arr)

    return merge_sort_result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    result = merge_sort(arr)

    mid = len(result) // 2

    print(f'#{tc} {result[mid]} {cnt}')


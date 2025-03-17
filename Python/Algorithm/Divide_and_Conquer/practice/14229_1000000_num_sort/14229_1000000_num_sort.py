# import sys
# sys.stdin = open("input.txt", "r")


def hoare_partition(left, right):
    pivot = arr[left]  # 피벗을 가장 왼쪽 요소로 설정
    i = left + 1  # 왼쪽에서 오른쪽으로 탐색할 인덱스
    j = right  # 오른쪽에서 왼쪽으로 탐색할 인덱스

    while i <= j:  # i와 j가 교차할 때까지 반복
        while i <= j and arr[i] <= pivot:  # 피벗보다 큰 값을 찾을 때까지 i 증가
            i += 1

        while i <= j and arr[j] >= pivot:  # 피벗보다 작은 값을 찾을 때까지 j 감소
            j -= 1

        if i < j:  # i와 j가 교차하지 않는다면
            arr[i], arr[j] = arr[j], arr[i]  # 두 요소를 교환

    arr[left], arr[j] = arr[j], arr[left]  # 피벗과 j 위치의 요소를 교환

    return j  # 피벗의 최정 위치 반환


def quick_sort(left, right):
    if left < right:
        # Hoare-Partition 알고리즘 사용
        pivot = hoare_partition(left, right)  # 배열을 분할하고 피벗 위치 반환

        quick_sort(left, pivot - 1)  # 피벗 왼쪽 부분 정렬
        quick_sort(pivot + 1, right)  # 피벗 오른쪽 부분 정렬


arr = list(map(int, input().split()))
quick_sort(0, 999999)

print(arr[500000])
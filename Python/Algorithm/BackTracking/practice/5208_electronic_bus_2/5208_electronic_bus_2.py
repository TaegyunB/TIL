import sys
sys.stdin = open("input1.txt", "r")

def f(i):
    """
    그리디 알고리즘으로 최소 충전 횟수를 구하는 재귀 함수
    i: 현재 정류장 위치
    """
    global cnt

    # 현재 정류장에서 현재 배터리로 바로 좋ㅇ점에 도달할 수 있는 경우 종료
    if i + arr[i] >= N-1:
        return

    max_able_to_go = 0  # 충전 후 가장 멀리 갈 수 있는 거리
    station = 0  # 다음에 이동할 정류장 위치

    # 현재 배터리로 갈 수 있는 모든 정류장 탐색
    for j in range(i+1, i+arr[i]+1):
        # j번 정류장에서 충전 후 갈 수 있는 거리가 더 멀다면 업데이트
        if max_able_to_go < j + arr[j]:
            max_able_to_go = j + arr[j]  # 최대 도달 가능 거리 업데이트
            station = j  # 다음 정류장 위치 저장

    cnt += 1  # 충전 횟수 증가
    f(station)  # 다음으로 선택된 정류장으로 이동


T = int(input())

for tc in range(1, T+1):
    N, *arr = map(int, input().split())
    cnt = 0

    f(0)

    print(f'#{tc} {cnt}')
import sys
sys.stdin = open("input.txt", "r")

def f(k, N, M):  # 이전까지의 교환횟수
    global max_v
    if k == N:  # 주어진 교환 횟수 사용
        tmp = int(''.join(card))

        if max_v < tmp:
            max_v = tmp

    else:
        for i in range(M-1):
            for j in range(1+1, M):  # 왜 1+1에서 시작?
                card[i], card[j] = card[j], card[i]
                tmp = int(''.join(card))

                if tmp not in memo[k]:
                    memo[k].append(tmp)
                    f(k+1, N, M)
                card[i], card[j] = card[j], card[i]


T = int(input())

for tc in range(1, T+1):
    num, N = input().split()
    card = list(num)
    N = int(N)
    M = len(card)
    max_v = 0  # 최대상금
    memo = [[] for _ in range(N)]  # memo[k] 행이 k번 교환에서 만들어지는 숫자를 저장
    f(0, N, M)
    print(f'#{tc} {max_v}')

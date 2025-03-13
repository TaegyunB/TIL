# 주사위 3개를 던져 나올 수 있는 모든 조합을 출력
# 종료조건: 주사위 3개를 던졌을 때
# branch: 1~6 숫자

dice = [1, 2, 3, 4, 5, 6]
n = 3
path = []

def recur(cnt, start):
    if cnt == n:
        print(*path)
        return

    for i in range(start, 7):
        path.append(i)
        recur(cnt + 1, i)
        path.pop()

recur(0, 1)
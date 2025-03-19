# import sys
# sys.stdin = open("input.txt", "r")

# 재귀적으로 원소 x가 속한 집합의 대표 원소를 찾음
def find_set_recur(x):
    if rep[x] == x:  # x가 자기 자신을 가리키고 있다면, x는 대표 원소이므로 그대로 반환
        return x
    else:
        rep[x] = find_set_recur(rep[x])  # 집합 내의 원소라면 대표원소를 직접 가리키도록 경로를 압축(path compression)
        return rep[x]


# 반복문을 사용하여 원소 x가 속한 집합의 대표 원소를 찾음
def find_set(x):
    while rep[x] != x:  # x가 자기 자신을 가리킬 때까지 반복적으로 상위 원소를 찾아감
        x = rep[x]
    return x


# 이 함수는 두 집합을 합치는 연산을 수행함
def union(x, y):  # y가 속한 집합의 대표원소가 x가 속한 집합의 대표원소를 가리키게 함
    rep[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    std_num, pair = map(int, input().split())
    pair_list = list(map(int, input().split()))

    # 1~std_num번이 대표 원소로 초기화: make_set(1) ~ make_set(std_num)
    rep = [i for i in range(std_num+1)]

    for i in range(pair):
        a, b = pair_list[2*i], pair_list[2*i+1]
        union(a, b)

    for i in range(std_num+1):
        find_set_recur(i)

    result = len(set(rep)) - 1  # 대표원소 중복을 제거한 후 맨 앞에 0번 인원은 없으므로 1을 뺌
    print(f'#{tc} {result}')
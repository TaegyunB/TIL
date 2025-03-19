# make_set(0)~make_set(5)
N = 6   # 원소 개수
rep = [i for i in range(N)]

# find_set(x)
def find_set(x):
    while rep[x]!=x:    # 자기자신을 가리키면 대표원소
        x = rep[x]
    return x

def find_set_recur(x):
    if rep[x]==x:   # 대표원소인 경우
        return x
    else:
        rep[x] = find_set_recur(x)  # 중간에 있는 원소가 대표를 직접 가리키도록 변경 (경로 단축)
        return rep[x]

# union(x, y)
# y가 속한 집합의 대표원소가 x가 속한 집합의 대표원소를 가르키게 함
def union(x, y):
    rep[find_set(y)] = find_set(x)
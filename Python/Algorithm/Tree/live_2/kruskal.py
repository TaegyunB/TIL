import sys
sys.stdin = open("graph.txt", "r")

# 크루스칼
# - 모든 간선들을 보면서
#  - 가중치가 작은 간선부터 고르자 (정렬)
#  - 이 때, 사이클이 발생하면 pass


def find_set(x):  # 대표자 검색
    if x == parents[x]:
        return x

    # 기본 코드
    # return find_set(parents[x])

    # 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    # 사이클 방지
    if ref_x == ref_y:
        return

    # 일정한 규칙으로 연결하자.
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y



V, E = map(int, input().split())
edges = []
for _ in range(E):
    start, end, weight = map(int, input().split())
    # 간선에 대한 정보들을 저장함
    edges.append((start, end, weight))

edges.sort(key=lambda x: x[2])  # 가중치 기준으로 오름차순
parents = [i for i in range(V)]  # make_set (정점을 기준으로 만들어준다)

# 작은 것부터 고르면서 나아가자
# 언제까지? N-1 개를 선택할 때 까지
cnt = 0     # 현재까지 선택한 간선의 수
result = 0  # MST 가중치의 합

for u, v, w in edges:
    # u 와 v 가 연결이 안되어있으면 선택
    #  == 다른 집합이라면 연결
    if find_set(u) != find_set(v):
        print(u, v, w)
        union(u, v)
        cnt += 1
        result += w

        if cnt == V - 1:  # MST 구성이 끝났다.
            break

print(result)
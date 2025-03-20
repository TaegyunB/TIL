# import sys
# sys.stdin = open("input1.txt", "r")

def find_set(x):
    while rep[x] != x:  # 대표원소를 찾을 때 까지
        x = rep[x]  # x의 대표자를 찾아서 이동
    return x  # 최종 대표자 반환


def union(x, y):
    rep[find_set(y)] = find_set(x)  # y의 대표자를 x의 대표자로 변경하여 두 집합 합치기


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]  # 노드 n1, n2, 가중치 w

    # Kruskal 적용
    # 가중치 기준 오름차순 정렬
    edge.sort(key = lambda x:x[2])  # 정렬 기준으로 지정하는 람다함수
    """
    - lambda x:x[2]는 각 간선 리스트 x에서 세 번째 요소를 반환함
    - 따라서 세 번째 요소를 기준으로 오름차순 정렬함
    """

    # 서로소 집합 (대표원소 집합)
    rep = [i for i in range(V+1)]  # 0번부터 V번까지의 노드

    # 0~V번 정점, 정점수 V+1개, 신장크리의 간선 수 V개
    cnt = 0  # 선택한 간선 수
    total = 0  # MST 가중치의 합

    for n1, n2, w in edge:  # 오름차순 정렬된 순으로 꺼내서
        if find_set(n1) == find_set(n2):  # 사이클 확인
            continue  # 사이클이 생기는 경우

        total += w
        union(n1, n2)
        cnt += 1

        if cnt == V:  # MST 구성 완료
            break

    print(f'#{tc} {total}')


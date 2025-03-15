import sys
sys.stdin = open("input1.txt", "r")

# 후위 순회
def postorder(M):

    # 노드가 유효한 범위를 벗어나면 0 반환
    if M > N:
        return 0

    # 이미 값이 있는 노드면 그 값을 반환
    if tree[M] != 0:
        return tree[M]

    left = postorder(M*2)  # 왼쪽 자식 노드의 합 계산
    right = postorder(M*2+1)  # 오른쪽 자식 노드의 합 계산
    tree[M] = left + right  # 현재 노드에 자식 노드들의 합 저장

    return tree[M]


T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for _ in range(M):
        node_num, num = map(int, input().split())

        tree[node_num] = num

    postorder(1)  # 루트 노드(1번)부터 재귀적으로 모든 노드의 값 계산

    print(f'#{tc} {tree[L]}')
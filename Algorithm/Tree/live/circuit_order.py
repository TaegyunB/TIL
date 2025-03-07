def pre_order(T):  # 전위순회, 방문한 정점(부모) 먼저 처리
    if T:  # 0이 아니면 (존재하는 정점이면)
        print(T)  # visit(T) T에서 할일 처리
        pre_order(left[T])  # 왼쪽 자식(서브트리)로 이동
        pre_order(right[T])  # 오른쪽 자식(서브트리)로 이동

def in_order(T):  # 중위순회
    if T:  # 0이 아니면 (존재하는 정점이면)
        in_order(left[T])  # 왼쪽 자식(서브트리)로 이동
        print(T)  # visit(T) T에서 할일 처리
        in_order(right[T])  # 오른쪽 자식(서브트리)로 이동

def post_order(T):  # 후위순회
    if T:  # 0이 아니면 (존재하는 정점이면)
        post_order(left[T])  # 왼쪽 자식(서브트리)로 이동
        post_order(right[T])  # 오른쪽 자식(서브트리)로 이동
        print(T)  # visit(T) T에서 할일 처리


N = int(input())
E = N - 1  # 간선의 수
arr = list(map(int, input().split()))

left = [0] * (N+1)  # 각 노드의 왼쪽 자식을 저장하는 배열. 인덱스는 부모 노드 번호
right = [0] * (N+1)  # 각 노드의 오른쪽 자식을 저장하는 배열. 인덱스는 부모 노드 번호
par = [0] * (N+1)  # 각 노드의 부모를 저장하는 배열. 인덱스는 자식 노드 번호

for i in range(E):  # 모든 간선에 대해 반복
    p, c = arr[i*2], arr[i*2+1]
    par[c] = p  # 자식 노드의 부모를 저장

    if left[p] == 0:  # 왼쪽자식이 아직 없으면
        left[p] = c
    else:
        right[p] = c

print(left)
print(right)

root = 1
for i in range(1, N+1):
    if par[i] == 0:  # 부모 정점이 없으면 루트
        root = i  # 발견한 루트 노드를 root 변수에 저장
        break  # 루트 노드를 찾았으므로 반복문을 종료
pre_order(root)  # 1번부터 전위순회
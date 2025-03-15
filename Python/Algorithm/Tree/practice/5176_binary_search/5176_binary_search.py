import sys
sys.stdin = open("input1.txt")

# 중위 순회
def inorder(num):
    global last

    if num <= N:  # 현재 노드 번호가 유효한 범위 내인지 확인
        inorder(num*2)  # 왼쪽 서브트리 중위 순회
        last += 1  # 순회 순서 카운터 증가
        tree[num] = last  # 현재 노드에 순회 순서 번호 저장
        inorder(num*2+1)  # 오른쪽 서브트리 중위 순회


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    last = 0

    inorder(1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')





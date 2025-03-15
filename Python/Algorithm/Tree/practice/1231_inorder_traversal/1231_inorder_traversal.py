import sys
sys.stdin = open("input.txt", "r")

def inorder(n):
    if n <= N:
        inorder(n*2)  # 왼쪽
        print(node_list[n], end="")
        inorder(n*2+1)  # 오른쪽


T = 10

for tc in range(1, T+1):
    N = int(input())  # 정점의 총 수
    node_list = [0] * (N+1)

    for i in range(1, N+1):
        node_num, alp, *pos = input().split()

        node_list[int(node_num)] = alp

    print(f'#{tc} ', end="")
    inorder(1)
    print()

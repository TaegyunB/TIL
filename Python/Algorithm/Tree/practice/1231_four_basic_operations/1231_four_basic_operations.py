import sys
sys.stdin = open("input.txt", "r")

def postorder(num):
    global result

    if num > N:
        return 0

    left = postorder(num*2)
    right = postorder(num*2+1)

    if tree[num] == '+':
        tree[num] = tree[left] + tree[right]

    elif tree[num] == '-':
        tree[num] = tree[left] - tree[right]

    elif tree[num] == '*':
        tree[num] = tree[left] * tree[right]

    elif tree[num] == '/':
        if tree[right] == 0:
            tree[num] = 0
        else:
            tree[num] = int(tree[left] / tree[right])

    return num


T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    result = 0

    for i in range(N):
        node_num, ele, *node = input().split()

        if ele not in '+-*/':
            tree[int(node_num)] = int(ele)
        else:
            tree[int(node_num)] = ele

    postorder(1)

    print(f'#{tc} {tree[1]}')



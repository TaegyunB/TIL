import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]

'''
경우의 수를 다 봐야함 -> DFS
DFS, BFS를 같이 사용해야함



'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    V = [0] * (N+1)  # 부피
    C = [0] * (N+1)  # 가치
    for i in range(1, N+1):
        V[i], C[i] = map(int, input().split())
    # dp[i][j] : i물건까지 고려해 부피 j를 채웠을 때의 최대가치
    dp = [[0]*(K+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, K+1):
            # 배낭보다 물건이 큰 경우
            if V[i] > j:
                dp[i][j] = dp[i-1][j]  # i물건없이 j를 채운경우
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-V[i]] + C[i])
    print(f'#{tc} {dp[N][K]}')
def f(i, N, K):  # p[i]를 결정하는 함수
    if i == K:  # 결정이 끝나면
        print(p)

    else:
        for j in range(N):  # used에서 사용하지 않은 숫자 확인
            if used[j] == 0:  # p에 a[j]가 들어있지 않으면
                used[j] = 1
                p[i] = a[j]
                f(i+1, N, K)
                used[j] = 0


a = [1, 2, 3, 4, 5]
N = len(a)
K = 3  # N개 중에 K개를 골라 만든 순열
p = [0] * K
used = [0] * N
f(0, N, K)